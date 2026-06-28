import pyodbc


class SQLServerConnection:

    def __init__(
        self,
        server,
        database,
        username=None,
        password=None,
        trusted_connection=False
    ):

        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.trusted_connection = trusted_connection
        self.conn = None


    def _build_connection_string(self):

        driver = "{ODBC Driver 17 for SQL Server}"

        if self.trusted_connection:

            return (
                f"DRIVER={driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"Trusted_Connection=yes;"
            )

        else:

            return (
                f"DRIVER={driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"
            )


    def connect(self):

        try:

            connection_string = self._build_connection_string()

            self.conn = pyodbc.connect(connection_string)

            print("Conexion exitosa con SQL Server")

            return self.conn

        except Exception as e:

            print(
                f"Error al conectar con SQL Server: {e}"
            )

            raise


    def execute_query(
        self,
        query,
        params=None
    ):

        if not self.conn:
            self.connect()

        try:

            with self.conn.cursor() as cursor:

                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                return cursor.fetchall()

        except Exception as e:

            print(
                f"Error al ejecutar consulta: {e}"
            )

            raise


    def execute_non_query(
        self,
        query,
        params=None
    ):

        if not self.conn:
            self.connect()

        try:

            with self.conn.cursor() as cursor:

                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                self.conn.commit()

                print("Operacion realizada correctamente")

        except Exception as e:

            if self.conn:
                self.conn.rollback()

            print(
                f"Error al ejecutar comando: {e}"
            )

            raise


    def close(self):

        if self.conn:

            self.conn.close()

            print(
                "Conexion cerrada"
            )