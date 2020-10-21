from pprint import pprint

from app.settings.consts import DEBUG, USER_IDS


def logger(msg):
    if DEBUG:
        pprint(msg)


def check_auth(user_id):
    return user_id in USER_IDS