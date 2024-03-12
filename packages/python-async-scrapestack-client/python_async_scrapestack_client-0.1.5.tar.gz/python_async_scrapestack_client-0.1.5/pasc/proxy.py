import asyncio
from asyncio import TimeoutError
from time import perf_counter
from aiohttp import ClientSession, ClientTimeout
from pasc.model import RequestBatch, ResultBatch, ClientRequest, ClientResult

SCRAPESTACK_URL = "https://api.scrapestack.com/scrape"

# todo: add parsing/model validation


async def __async_request(
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
            status = int(str(response.status))  # todo: fix patch later
            duration = perf_counter() - start
            if request.parser is not None:
                data = request.parser(data)
            if request.validator is not None:
                data = request.validator.model_validate(data)
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
                group=request.group,
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
            group=request.group,
        )


async def __async_execute_batch(batch: RequestBatch, secret: str) -> ResultBatch:
    global_start = perf_counter()
    async with ClientSession() as session:
        tasks = list()
        for request in batch.requests:
            task = asyncio.ensure_future(
                __async_request(
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


# todo: implement
# todo: docstrings
def execute_one(
    request: ClientRequest,
    secret: str,
) -> ClientResult:
    raise NotImplementedError()


# todo: docstring example
def execute_batch(
    batch: RequestBatch,
    secret: str,
) -> ResultBatch:
    """
    Execute a batch of requests outside a running event loop (eg: jupyter, uvicorn).

    Args:
        batch (RequestBatch): a batch of requests
        secret (str): scrapestack api key

    Returns:
        ResultBatch: a batch of results
    """
    return asyncio.run(__async_execute_batch(batch, secret))


# todo: implement
# todo: docstring details
def el_execute_one(
    request: ClientRequest,
    secret: str,
) -> ClientResult:
    """
    Execute a single request inside a running event loop (eg: jupyter, uvicorn).

    Args:
        request (ClientRequest): _description_
        secret (str): _description_

    Returns:
        ClientResult: _description_

    Usage:

    ```python
    from pasc import proxy, ClientRequest
    request = ClientRequest(target="https://en.wikipedia.org", method="GET")
    result = await proxy.el_execute_one(request=request, secret="<your API key>")
    ```
    """
    raise NotImplementedError()


# todo: docstrings
def el_execute_batch(
    batch: RequestBatch,
    secret: str,
) -> ResultBatch:
    return __async_execute_batch(batch, secret)
