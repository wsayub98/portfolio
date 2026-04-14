from psycopg2.extras import RealDictCursor
from core.database import Database


class PortfolioRepository:

    @staticmethod
    def get_all():
        # Connect to an existing database.
        conn = Database.connect()
        # Open a cursor to perform database operations
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # cur = conn.cursor()
        # Execute command
        sql = "SELECT id, name, experience, skills, companies FROM portfolios LIMIT 1;"
        cur.execute(sql)
        # Obtain data
        rows = cur.fetchall()
        # Close connection
        cur.close()
        conn.close()

        return rows
