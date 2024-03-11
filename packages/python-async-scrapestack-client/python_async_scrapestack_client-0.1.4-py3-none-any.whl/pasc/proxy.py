import asyncio
from asyncio import TimeoutError
from time import perf_counter
from aiohttp import ClientSession, ClientTimeout
from pasc.model import RequestBatch, ResultBatch, ClientRequest, ClientResult

SCRAPESTACK_URL = "https://api.scrapestack.com/scrape"


async def async_request(
    session: ClientSession,
    request: ClientRequest,
    secret: str,
) -> ClientResult:
    start = perf_counter()
    methods = {"GET": session.get, "POST": session.post}
    try:
        async with methods[request.method](
            SCRAPESTACK_URL,
            headers=request.headers,
            cookies=request.cookies,
            timeout=ClientTimeout(total=request.timeout),
            params={
                "access_key": secret,
                "url": request.url,
                "premium_proxy": 1 if request.premium else 0,
                "keep_headers": 1 if request.headers is not None else 0,
            },
        ) as response:
            data = await response.read()
            status = int(str(response.status))
            duration = perf_counter() - start
            return ClientResult(
                target=request.target,
                method=request.method,
                params=request.params,
                headers=request.headers,
                cookies=request.cookies,
                timeout=request.timeout,
                status=int(status),
                duration=duration,
                data=data,
            )
    except TimeoutError:
        duration = perf_counter() - start
        return ClientResult(
            target=request.target,
            method=request.method,
            params=request.params,
            headers=request.headers,
            cookies=request.cookies,
            timeout=request.timeout,
            status=408,
            duration=duration,
            data=None,
        )


async def execute_batch(batch: RequestBatch, secret: str) -> ResultBatch:
    global_start = perf_counter()
    async with ClientSession() as session:
        tasks = list()
        for request in batch.requests:
            task = asyncio.ensure_future(
                async_request(
                    session,
                    request,
                    secret,
                )
            )
            tasks.append(task)
        results = await asyncio.gather(*tasks)
    return ResultBatch(
        results=results,
        duration=perf_counter() - global_start,
    )


def execute(
    batch: RequestBatch,
    secret: str,
) -> ResultBatch:
    """
    _summary_

    Args:
        batch (RequestBatch): _description_
        secret (str): Scrapestack API/access key.
        verbose (bool, optional): Show progress bar. Defaults to False.

    Returns:
        ResultBatch: _description_
    """
    return asyncio.run(execute_batch(batch, secret))


def execute_in_event_loop(
    batch: RequestBatch,
    secret: str,
) -> ResultBatch:
    """
    _summary_

    Args:
        batch (RequestBatch): _description_
        secret (str): Scrapestack API/access key.
        verbose (bool, optional): Show progress bar. Defaults to False.

    Returns:
        ResultBatch: _description_
    """
    return execute_batch(batch, secret)
