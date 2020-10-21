from pprint import pprint

from app.settings.consts import DEBUG


def logger(msg):
    if DEBUG:
        pprint(msg)

