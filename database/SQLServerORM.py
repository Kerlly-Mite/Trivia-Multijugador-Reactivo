import urllib

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()


class SQLServerORM:
    """
    Envoltorio asíncrono sobre SQLAlchemy + aioodbc para SQL Server.

    Usa create_async_engine en vez de create_engine, y AsyncSession
    en vez de Session, para que todas las transacciones del ORM
    sean no bloqueantes.
    """

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

        self.engine = None
        self.Session = None

        self._create_engine()

    def _create_engine(self):

        driver = "ODBC Driver 17 for SQL Server"

        if self.trusted_connection:

            params = (
                f"DRIVER={driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"Trusted_Connection=yes;"
            )

        else:

            params = (
                f"DRIVER={driver};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"
            )

        params_encoded = urllib.parse.quote_plus(
            params
        )

        connection_url = (
            f"mssql+aioodbc:///?odbc_connect={params_encoded}"
        )

        try:

            self.engine = create_async_engine(
                connection_url,
                echo=False
            )

            self.Session = sessionmaker(
                bind=self.engine,
                class_=AsyncSession,
                expire_on_commit=False
            )

            print(
                "Motor ORM asincrono configurado correctamente"
            )

        except Exception as e:

            print(
                f"Error al crear el ORM: {e}"
            )

            raise

    def get_session(self):

        if not self.Session:

            raise Exception(
                "El ORM no se encuentra inicializado"
            )

        return self.Session()
