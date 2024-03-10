import logging
from abc import ABC
from typing import Any

import requests
from pydantic import HttpUrl

from .utils import get_logger
from .utils.logs import get_nonce, shortify_log_value


class BaseAPIClient(ABC):
    name: str
    _base_url: HttpUrl
    _session: requests.Session
    _nonce: str
    _logger: logging.Logger

    def __init__(self, nonce: str = ""):
        self._nonce = nonce or get_nonce()
        self._session = requests.Session()
        self._logger = get_logger("APIClient")

    def post(self, endpoint: str, *, json: Any = None, data: Any = None, **kwargs: Any) -> requests.Response:
        return self._request("POST", endpoint, json=json, data=data, **kwargs)

    def put(self, endpoint: str, *, json: Any = None, data: Any = None, **kwargs: Any) -> requests.Response:
        return self._request("PUT", endpoint, json=json, data=data, **kwargs)

    def get(self, endpoint: str, *, params: Any = None, **kwargs: Any) -> requests.Response:
        return self._request("GET", endpoint, params=params, **kwargs)

    def _make_full_url(self, endpoint: str) -> str:
        return f"{self._base_url}{endpoint}"

    def _request(self, method: str, endpoint: str, **kwargs: Any) -> requests.Response:
        full_url = self._make_full_url(endpoint)

        # Create the Request.
        req = requests.Request(
            method=method.upper(),
            url=full_url,
            headers=kwargs.get("headers"),
            files=kwargs.get("files"),
            data=kwargs.get("data"),
            json=kwargs.get("json"),
            params=kwargs.get("params"),
            auth=kwargs.get("auth"),
            cookies=kwargs.get("cookies"),
            hooks=kwargs.get("hooks"),
        )
        self.prepare_authentication(req)
        self._debug(f'Preparing {req.method} request to "{req.url}"', extra=req.__dict__)
        prepared_request: requests.PreparedRequest = self._session.prepare_request(req)

        self._info(
            f"Sending request with payload={prepared_request.body!r}",
            extra={"payload": shortify_log_value(kwargs.get("json", kwargs.get("data", {})))},
        )
        response = self._session.send(prepared_request)

        str_repr_content = response.content.decode("utf8")[:500]
        self._info(f"Response {response.status_code=} {str_repr_content=}", extra={"status_code": response.status_code, "content": str_repr_content})

        response.raise_for_status()
        return response

    def prepare_authentication(self, request: requests.Request) -> None:
        """Do auth setup in-place"""
        pass

    def _info(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._logger.info(f"[{self._nonce}] {msg}", *args, stacklevel=2, **kwargs)

    def _debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._logger.debug(f"[{self._nonce}] {msg}", *args, stacklevel=2, **kwargs)

    def _warn(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._logger.warning(f"[{self._nonce}] {msg}", *args, stacklevel=2, **kwargs)

    def _error(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._logger.error(f"[{self._nonce}] {msg}", *args, stacklevel=2, **kwargs)

    def _critical(self, msg: str, *args: Any, **kwargs: Any) -> None:
        self._logger.critical(f"[{self._nonce}] {msg}", *args, stacklevel=2, **kwargs)
