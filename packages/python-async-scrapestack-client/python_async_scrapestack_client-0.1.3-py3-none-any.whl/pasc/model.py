from __future__ import annotations
from pandas import DataFrame
from typing import Optional
from urllib.parse import urlencode
from typing import Literal, Any, Optional
from pydantic import BaseModel, model_validator


RequestMethod = Literal["GET", "POST"]


class ClientRequest(BaseModel):
    target: str
    params: Optional[dict] = None
    headers: Optional[dict] = None
    cookies: Optional[dict] = None
    method: RequestMethod
    timeout: int = 100
    premium: bool = False

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
        headers: Optional[dict] = None,
        cookies: Optional[dict] = None,
        timeout: int = 100,
    ) -> RequestBatch:
        """
        If everything besides the targets is the same,
        you can create a request batch here.
        """
        client_requests: list[ClientRequest] = [
            ClientRequest(
                target=target,
                method=method,
                headers=headers,
                cookies=cookies,
                timeout=timeout,
            )
            for target in targets
        ]
        return RequestBatch(requests=client_requests)


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
    data: Optional[bytes] = None


class ResultBatch(BaseModel):
    results: list[ClientResult]
    duration: float

    @property
    def dataframe(self) -> DataFrame:
        return DataFrame([result.model_dump() for result in self.results])
