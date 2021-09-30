from parking_system.utility.constants import DEFAULT_DB_CONNECTION_STRING
import peewee
import os
from parking_system.utility.logger import logger


def initalize_database():
    """
    Initialize database
    """

    try:
        connection_string = os.environ.get("DB_CONNECTION_STRING")
        if connection_string is None:
            connection_string = DEFAULT_DB_CONNECTION_STRING
        db = peewee.SqliteDatabase(connection_string, autoconnect=False)
        logger.info("Database initialization complete")
        return db
    except Exception as e:
        logger.error(e)
        raise (e)


db = initalize_database()
