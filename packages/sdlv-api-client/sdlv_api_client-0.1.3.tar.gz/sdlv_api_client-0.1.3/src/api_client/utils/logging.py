import dataclasses
import json
import logging
from dataclasses import asdict
from typing import Any
from uuid import uuid4

from .parse import APIClientJSONEncoder


def get_logger(name: str = "service") -> logging.Logger:
    return logging.getLogger(name)


def _shorten_dict_keys(dct: dict) -> dict:
    res = {}
    for k, v in dct.items():
        if isinstance(v, str) and len(v) > 64:
            v = f"{v[:30]}...{v[-30:]}"
        elif isinstance(v, dict):
            v = _shorten_dict_keys(v)
        res[k] = v
    return res


def shortify_log_value(dct: Any) -> str:
    if dataclasses.is_dataclass(dct):
        dct = asdict(dct)
    if not isinstance(dct, dict):
        return str(dct)
    return json.dumps(_shorten_dict_keys(dct), cls=APIClientJSONEncoder)


def get_nonce() -> str:
    return uuid4().hex[:12]
