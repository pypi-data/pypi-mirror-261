import datetime
import decimal
import json
from typing import Any

from pydantic import BaseModel

__all__ = [
    "APIClientJSONEncoder",
]


class APIClientJSONEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        try:
            if isinstance(obj, decimal.Decimal):
                return str(obj)
            if isinstance(obj, (datetime.datetime, datetime.date)):
                return obj.isoformat()
            if isinstance(obj, BaseModel):
                return obj.model_dump_json()
            if isinstance(obj, datetime.timedelta):
                return dict(__type__="timedelta", total_seconds=obj.total_seconds())
            if hasattr(obj, "as_dict"):
                if callable(getattr(obj, "as_dict")):
                    return super().default(obj.as_dict())
                return super().default(obj.as_dict)
            if isinstance(obj, set):
                return list(obj)
            if hasattr(obj, "__dict__"):
                return obj.__dict__
            return super().default(obj)
        except TypeError as exc:
            if "not JSON serializable" in str(exc):
                return str(obj)
            raise exc
