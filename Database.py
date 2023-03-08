import psycopg2

class Database:
    def __init__(self, host, port, dbname, user, password):
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )

    def execute_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            self.conn.commit()
            result = cur.fetchall()
            cur.close()

        return result