from app.db.wrappers import MongoDB

DBS = {}


def init_databases(config):
    """
    Usage example
    DBS["clickhouse"] = await ClickHouse.init_async(config["clickhouse"])
    DBS["mysql"] = await MySQL.init_async(config["mysql"])
    """
    DBS["mongo"] = MongoDB.init(config["mongo"])


def shutdown_databases():
    """
    await ClickHouse.close_async(DBS["clickhouse"])
    await MySQL.close_async(DBS["mysql"])
    """
    MongoDB.close(DBS["mongo"])
