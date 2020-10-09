from pathlib import Path

from envparse import env

DEBUG = env("DEBUG", default=False)

ROOT_DIR = Path(__name__).parent.parent
CONFIG_DIR = ROOT_DIR / "config"

VERSION = "2020.06.09"
SERVICE_NAME = "physics"

MSG_SERVICE_DESCRIPTION = "physics tg bot for a good mark"
