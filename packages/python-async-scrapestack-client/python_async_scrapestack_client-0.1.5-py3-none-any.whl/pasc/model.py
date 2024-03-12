from __future__ import annotations
from pandas import DataFrame
from typing import Optional, Callable
from urllib.parse import urlencode
from typing import Literal, Any, Optional, Type
from pydantic import BaseModel, model_validator


RequestMethod = Literal["GET", "POST"]


# todo: add id, uuid4
# todo: add hash of request for identification of redundant
# todo: add timestamp for timestamp request sent at
# todo: add model validator to extract params from target to increase determinism
# * params added back in @ url property call
class ClientRequest(BaseModel):
    target: str
    method: RequestMethod
    params: Optional[dict] = None
    headers: Optional[dict] = None
    cookies: Optional[dict] = None
    timeout: int = 100
    premium: bool = False
    parser: Optional[Callable[[bytes], dict]] = None
    validator: Optional[Type[BaseModel]] = None
    group: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def __validate_method(cls, data: Any) -> Any:
        if isinstance(data, dict):
            data["method"] = data["method"].upper()
        return data

    @property
    def url(self) -> str:
        if isinstance(self.params, dict):
            return f"{self.target}?{urlencode(self.params)}"
        else:
            return self.target


class RequestBatch(BaseModel):
    requests: list[ClientRequest]

    @staticmethod
    def create(
        targets: list[str],
        method: RequestMethod,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        cookies: Optional[dict] = None,
        timeout: int = 100,
        premium: bool = False,
        parser: Optional[Callable[[bytes], dict]] = None,
        validator: Optional[Type[BaseModel]] = None,
        group: Optional[str] = None,
    ) -> RequestBatch:
        """
        If everything besides the targets is the same,
        you can create a request batch here.
        """
        client_requests: list[ClientRequest] = [
            ClientRequest(
                target=target,
                method=method,
                params=params,
                headers=headers,
                cookies=cookies,
                timeout=timeout,
                premium=premium,
                parser=parser,
                validator=validator,
                group=group,
            )
            for target in targets
        ]
        return RequestBatch(requests=client_requests)

    @staticmethod
    def concat(batches: list[RequestBatch]) -> RequestBatch:
        requests = list()
        for batch in batches:
            requests.extend(batch.requests)
        return RequestBatch(requests=requests)


class ClientResult(BaseModel):
    target: str
    method: RequestMethod
    params: Optional[dict] = None
    headers: Optional[dict] = None
    cookies: Optional[dict] = None
    timeout: int = 100
    premium: bool = False
    status: int
    duration: float
    data: Optional[bytes | dict | BaseModel] = None
    group: Optional[str] = None


class ResultBatch(BaseModel):
    results: list[ClientResult]
    duration: float

    @property
    def dataframe(self) -> DataFrame:
        return DataFrame([result.model_dump() for result in self.results])
