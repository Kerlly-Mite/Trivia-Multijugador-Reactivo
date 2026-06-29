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

    async def connect(self):

        import aioodbc

        try:

            connection_string = self._build_connection_string()

            self.conn = await aioodbc.connect(
                dsn=connection_string,
                autocommit=False
            )

            print("Conexion asincrona exitosa con SQL Server")

            return self.conn

        except Exception as e:

            print(
                f"Error al conectar con SQL Server: {e}"
            )

            raise

    async def execute_query(
        self,
        query,
        params=None
    ):

        if not self.conn:
            await self.connect()

        try:

            async with self.conn.cursor() as cursor:

                if params:
                    await cursor.execute(query, params)
                else:
                    await cursor.execute(query)

                filas = await cursor.fetchall()

                return filas

        except Exception as e:

            print(
                f"Error al ejecutar consulta: {e}"
            )

            raise

    async def execute_non_query(
        self,
        query,
        params=None
    ):

        if not self.conn:
            await self.connect()

        try:

            async with self.conn.cursor() as cursor:

                if params:
                    await cursor.execute(query, params)
                else:
                    await cursor.execute(query)

                await self.conn.commit()

                print("Operacion realizada correctamente")

        except Exception as e:

            await self.conn.rollback()

            print(
                f"Error al ejecutar comando: {e}"
            )

            raise

    async def close(self):

        if self.conn:

            await self.conn.close()

            print(
                "Conexion cerrada"
            )
