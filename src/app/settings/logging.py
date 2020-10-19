import sys
import sentry_sdk
from envparse import env
import logging
from fluent import handler
from loguru import logger

from .consts import SERVICE_NAME, VERSION

def init_logging():
    env.read_envfile()
    docker_host = env("DOCKER_HOST", default=None)
    routing_name = f"log.{SERVICE_NAME}.{docker_host}" if docker_host else f"log.{SERVICE_NAME}"
    print(routing_name)

    def format_logrecord(log_record):
        record = log_record.extra

        record["args"] = log_record.args
        record["created"] = log_record.created
        record["filename"] = log_record.filename
        record['funcName'] = log_record.funcName
        record['hostname'] = log_record.hostname
        record['levelname'] = log_record.levelname
        record["message"] = log_record.message

        return record

    formatter = format_logrecord
    formatter.usesTime = lambda : False

    config = {
        "handlers": [
            {
                "sink": sys.stdout,
                "format": "{time} - {level} - {function} : {message}\n{extra}",
            },
            {"sink": f"logs/{SERVICE_NAME}.log", "serialize": True},
        ],
        "activation": [
            ("uvicorn.access", True),
            ("uvicorn.error", False),
            ("uvicorn.asgi", False),
            ("fluent.test", True)
        ],
        "extra": {"user": SERVICE_NAME},
    }
    logger.configure(**config)


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentaion.
    See https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )


async def format_log_message(request, response, has_body=True):
    return dict(request)


def logger(message, *args, log_on=True, level='info', **kwargs):
    if log_on:
        getattr(loguru_logger.bind(
            **{}
        ), level.lower())(message, *args, **kwargs)
