import os

from sqlalchemy import engine_from_config, URL
import logging

logger = logging.getLogger(__name__)

class SourceConfig(object):

    def __init__(self, drivername, host, port, database, username, password):
        self.url = URL.create(
            drivername=drivername,
            username=username,
            password=password,
            host=host,
            database=database
        )
        self.pool_size = None
        self.max_overflow = None
        self.db_schema = None

    def set_pool_size(self, size: int):
        self.pool_size = size

    def set_max_overflow(self, max_overflow: int):
        self.max_overflow = max_overflow


class DBConnection:

    def __init__(self, db_cfg: SourceConfig = None):
        self.DB_DRIVER_NAME = os.getenv("DB_DRIVER_NAME")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DB_DATABASE = os.getenv("DB_DATABASE")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")

        self.db_connection = self.get_db_connection()

    def get_db_connection(self):
        obj = self.get_db_connection()
        logger.info(f"DB_AUTH_TYPE: {obj.DB_AUTH_TYPE}")

        db_cfg = SourceConfig(drivername=self.DB_DRIVER_NAME, host=self.HOST, port=self.PORT,
                          database=self.DATABASE, password=self.PASSWORD)

        return db_cfg