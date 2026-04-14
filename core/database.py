import psycopg2
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Database:

    @staticmethod
    def connect():
        # db_username, db_password, db_name, db_host, db_port
        return psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )

    # refactor to centralize con, cur and query execution to commit, fetch.
