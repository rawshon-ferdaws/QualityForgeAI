class DBClient:

    def __init__(self, connection=None):
        self.connection = connection

    def execute_query(self, query):
        if self.connection is None:
            raise ConnectionError("Database connection is not configured")

        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
