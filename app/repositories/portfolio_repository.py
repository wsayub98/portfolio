import psycopg2
from psycopg2.extras import RealDictCursor
from devtools import debug


class PortfolioRepository:
    """
    FETCH portfolio
    """

    @staticmethod
    def get_all(conn):
        cur = conn.cursor(cursor_factory=RealDictCursor)
        # cur = conn.cursor()
        # Execute command
        sql = "SELECT id, name, experience, skills, companies FROM portfolios LIMIT 1;"
        cur.execute(sql)
        # Obtain data
        rows = cur.fetchall()
        # Close connection
        cur.close()

        return rows[0]

    """
    UPDATE portfolio
    """

    @staticmethod
    def update(conn: psycopg2.extensions.connection, params):
        cur = conn.cursor(cursor_factory=RealDictCursor)
        field = []
        values = []
        for key, value in params.items():
            if key in ["id"]:
                continue
            field.append(f"{key} = %s")
            values.append(value)

        set_clause = ", ".join(field)
        values.append(params["id"])
        sql = f"UPDATE portfolios SET {set_clause} WHERE id = %s"

        cur.execute(sql, values)
        updated_row_count = cur.rowcount
        cur.close()

        return updated_row_count

    """
    CREATE portfolio
    """

    @staticmethod
    def create(conn: psycopg2.extensions.connection, params):
        cur = conn.cursor(cursor_factory=RealDictCursor)
        field = []
        values = []
        string_holder = []
        for key, value in params.items():
            if key in ["id"]:
                continue
            field.append(f"{key}")
            values.append(value)
            string_holder.append(f"%s")

        columns = ", ".join(field)
        placeholder = ", ".join(string_holder)
        sql = f"INSERT INTO portfolios ({columns}) VALUES ({placeholder}) RETURNING id, {columns}"

        cur.execute(sql, values)
        data = cur.fetchone()

        cur.close()

        return data

    """
    DELETE portfolio
    """

    @staticmethod
    def delete(conn: psycopg2.extensions.connection, params):
        cur = conn.cursor()
        debug(params)
        sql = f"DELETE FROM portfolios WHERE id = %s"

        cur.execute(sql, [params["id"]])
        deleted_row_count = cur.rowcount
        cur.close()

        return deleted_row_count
