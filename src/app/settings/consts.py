from pathlib import Path

from envparse import env

env.read_envfile()

DEBUG = env("DEBUG", default=False)

ROOT_DIR = Path(__name__).parent.parent
CONFIG_DIR = ROOT_DIR / "config"

VERSION = "2020.06.09"
SERVICE_NAME = "physics"

MSG_SERVICE_DESCRIPTION = "physics tg bot for a good mark"

TOKEN = env("BOT_TOKEN")

TABLE_URL = 'https://docs.google.com/spreadsheets/d/1dWyW47H6Qzk_k68ZHf7RXYc9-gq1FeXobWbp0iB5LmE/edit#gid=0'
TOTAL_DF_COL = 'Всего'

USER_ID = [
    197079657,  # Valya
    306633623  # Nikita
]

ERROR_PARSE_MESSAGE = 'Неправильное использование команды. Введите /help'
UNAUTHORIZED_USER_MESSAGE = 'Вы не добавили себе таблицу. /newGroup [group]'
SEARCH_NOT_FOUND_TEXT = 'По такой подстроке никого не найдено'
SUCCESSED_TEXT = 'Дело сделано'

DICT_OF_BUTTONS = {1: 'Добавить баллы',
                   2: ['Добавить новый класс', 'Начать новый урок']}
