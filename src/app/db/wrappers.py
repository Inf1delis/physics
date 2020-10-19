class ClickHouse:
    @staticmethod
    def read_settings_async():
        from envparse import env

        env.read_envfile()

        config = dict()
        config["url"] = env("CH_URL")
        config["user"] = env("CH_USER")
        config["password"] = env("CH_PASS")

        return config

    @staticmethod
    async def init_async(config):
        from aiohttp import ClientSession
        from aiochclient import ChClient as Client

        session = ClientSession()
        client = Client(session, **config)
        assert await client.is_alive()

        connect = {"client": client, "session": session}
        return connect

    @staticmethod
    async def close_async(connect):
        if not connect["session"].closed:
            await connect["session"].close()


class MySQL:
    @staticmethod
    def read_settings_async(connection_string=True):
        from envparse import env

        env.read_envfile()

        config = dict()
        mysql_user = env("MYSQL_USER", "")
        if mysql_user:
            config["user"] = mysql_user

        mysql_password = env("MYSQL_PASS", "")
        if mysql_password:
            config["password"] = mysql_password

        config["host"] = env("MYSQL_HOST")
        config["port"] = int(env("MYSQL_PORT"))

        config["db"] = env("MYSQL_DB")

        if connection_string:
            connection_string = "mysql://"
            for key, value in config.items():
                if key == "user":
                    connection_string += value
                elif key == "password":
                    connection_string += f":{value}"
                elif key == "host":
                    connection_string += f"@{value}"
                elif key == "port":
                    connection_string += f":{value}"
                elif key == "db":
                    connection_string += f"/{value}"
            return {"connection_string": connection_string}
        return config

    @staticmethod
    async def init_async(config):
        from databases import Database

        database = Database(
            config["connection_string"], minsize=0, maxsize=10, pool_recycle=30
        )
        await database.connect()

        return database

    @staticmethod
    async def close_async(connect):
        if connect.is_connected:
            await connect.disconnect()

    @staticmethod
    def read_settings():
        return MySQL.read_settings_async()

    @staticmethod
    def init(config):
        import MySQLdb

        config["autocommit"] = True
        connection = MySQLdb.connect(**config)
        cursor = connection.cursor()

        connect = {"connection": connection, "cursor": cursor}
        return connect

    @staticmethod
    def close(connect):
        connect["cursor"].close()


class MongoDB:
    @staticmethod
    def read_settings_async():
        from envparse import env

        env.read_envfile()

        config = dict()
        config["connection_string"] = env("MONGODB_CONNECTION_STRING")
        config["db"] = env("MONGODB_DB")

        return config

    @staticmethod
    async def init_async(config):
        import motor.motor_asyncio as aiomotor

        conn = aiomotor.AsyncIOMotorClient(config["connection_string"])
        db = conn[config["db"]]

        connect = {"client": db}
        return connect

    @staticmethod
    async def close_async(connect):
        connect["client"].client.close()

    @staticmethod
    def read_settings():
        from envparse import env

        env.read_envfile()

        config = dict()
        config["connection_string"] = env("MONGODB_CONNECTION_STRING")
        return config

    @staticmethod
    def init(config):
        from pymongo import MongoClient

        conn = MongoClient(config["connection_string"])
        db = conn.get_database()
        connect = {"client": db}
        return connect

    @staticmethod
    def close(connect):
        pass


if __name__ == "__main__":
    print(MySQL.read_settings_async())
