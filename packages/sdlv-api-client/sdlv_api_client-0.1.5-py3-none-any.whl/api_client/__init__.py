import logging.config

from .client import BaseAPIClient

__version__ = "0.1.5"
__all__ = ["BaseAPIClient"]

LOGGING: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {},
    "formatters": {
        "api-client.structured": {
            "()": "api_client.utils.APIClientLogJSONFormatter",
        },
        "api-client.simple": {
            "format": "[%(asctime)s] %(levelname)s: %(message)s",
            "datefmt": "%F %T",
        },
    },
    "handlers": {
        "api-client.structured": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "api-client.structured",
        },
    },
}
logging.config.dictConfig(LOGGING)
