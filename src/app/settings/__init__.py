from pathlib import Path

from envparse import env
from app.db.wrappers import MongoDB

from app.settings.consts import SERVICE_NAME, CONFIG_DIR
from app.utils.gtables import GTable

CONFIG = dict()


def load_config():

    # Delete what you don't need
    #CONFIG["clickhouse"] = ClickHouse.read_settings_async()
    #CONFIG["mysql"] = MySQL.read_settings_async()
    CONFIG["mongo"] = MongoDB.read_settings()
    CONFIG["bot_token"] = env('BOT_TOKEN')

    p = Path(__file__) / "../../config/service_account_credentials.json"
    p = str(p.resolve())

    gtable_credentials_path = p
    with open(gtable_credentials_path, 'w') as f:
        import json
        j = env('SERVICE_ACCOUNT_CREDENTIALS').encode('unicode_escape').decode('utf-8')
        j = j.replace('|', r'\n')
        j = json.loads(j)
        json.dump(j, f)

    CONFIG['gtable'] = GTable(env("GTABLE_KEY"), gtable_credentials_path)
