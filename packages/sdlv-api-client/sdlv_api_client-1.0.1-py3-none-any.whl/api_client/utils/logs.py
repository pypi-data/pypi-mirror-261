import dataclasses
import datetime
import json
import logging
import os
from dataclasses import asdict
from logging import LogRecord
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


class APIClientLogJSONFormatter(logging.Formatter):
    default_time_format = "%Y-%m-%d %H:%M:%S"

    def format(self, record: LogRecord) -> str:
        record_default_keys = [
            "name",
            "msg",
            "args",
            "levelname",
            "levelno",
            "pathname",
            "exc_info",
            "filename",
            "lineno",
            "funcName",
            "created",
            "msecs",
            "relativeCreated",
            "thread",
            "threadName",
            "processName",
            "process",
            "message",
            "asctime",
            "module",
            "exc_text",
            "stack_info",
        ]
        structured_data = dict(
            app=os.environ.get("APP_NAME", "dev"),
            level=record.levelname,
            name=record.name,
            date_time=datetime.datetime.fromtimestamp(record.created).strftime(self.default_time_format),
            location=f"{record.pathname or record.filename}:{record.funcName}:{record.lineno}",
            message=record.getMessage(),
            extra_data={k: record.__dict__[k] for k in record.__dict__.keys() if k not in record_default_keys},
        )

        return json.dumps(structured_data, cls=APIClientJSONEncoder)
