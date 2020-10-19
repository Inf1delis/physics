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

USER_ID = [
    197079657,  # Valya
    306633623   # Nikita
]

START_NEW_CLASS = 'Добавить новый класс'
START_NEW_LESSON = 'Начать новый урок'
