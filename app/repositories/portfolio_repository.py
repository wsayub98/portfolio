from psycopg2.extras import RealDictCursor


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
    def update_portfolio(conn, params):
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
        rowCount = cur.rowcount
        cur.close()

        return rowCount

    """
    CREATE portfolio
    """

    """
    DELETE portfolio
    """
