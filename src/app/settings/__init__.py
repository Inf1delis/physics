import yaml
from envparse import env
from app.db.wrappers import MongoDB

from app.settings.consts import SERVICE_NAME, CONFIG_DIR

CONFIG = dict()


def load_config():

    # Delete what you don't need
    #CONFIG["clickhouse"] = ClickHouse.read_settings_async()
    #CONFIG["mysql"] = MySQL.read_settings_async()
    CONFIG["mongo"] = MongoDB.read_settings()
    CONFIG["bot_token"] = env('BOT_TOKEN')
