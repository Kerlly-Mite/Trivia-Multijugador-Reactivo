from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import urllib

# Base para mapear las tablas a clases de Python
Base = declarative_base()

class SQLServerORM:
    def __init__(self, server, database, username=None, password=None, trusted_connection=False):
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
        
        # Formatear los parámetros para que sean seguros en una URL
        if self.trusted_connection:
            params = f"DRIVER={driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
        else:
            params = f"DRIVER={driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};"
        
        # SQLAlchemy requiere que la cadena de conexión ODBC se pase codificada en la URL
        params_encoded = urllib.parse.quote_plus(params)
        connection_url = f"mssql+pyodbc:///?odbc_connect={params_encoded}"
        
        try:
            # Crear el motor de conexión
            self.engine = create_engine(connection_url, echo=False) # echo=True mostrará el SQL en consola
            # Crear la fábrica de sesiones
            self.Session = sessionmaker(bind=self.engine)
            print("🚀 Motor ORM SQLAlchemy configurado correctamente.")
        except Exception as e:
            print(f"❌ Error al inicializar el motor ORM: {e}")
            raise

    def get_session(self):
        """Devuelve una nueva sesión para interactuar con la BD."""
        if not self.Session:
            raise Exception("El motor ORM no está inicializado.")
        return self.Session()

# --- MODO DE USO ---

# 1. Definir un modelo (Tabla)
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    email = Column(String(50))

if __name__ == "__main__":
    # 2. Inicializar el ORM (Autenticación Windows en este ejemplo)
    db_orm = SQLServerORM(
        server="localhost\\SQLEXPRESS",
        database="MiBaseDatos",
        trusted_connection=True
    )
    
    # 3. Operar con la base de datos usando una sesión
    session = db_orm.get_session()
    
    try:
        # Insertar un nuevo usuario
        nuevo_usuario = Usuario(nombre="Carlos", email="carlos@email.com")
        session.add(nuevo_usuario)
        session.commit() # Guarda cambios
        
        # Consultar usuarios
        usuarios = session.query(Usuario).filter(Usuario.nombre == "Carlos").all()
        for u in usuarios:
            print(f"ID: {u.id} - Nombre: {u.nombre}")
            
    except Exception as e:
        session.rollback()
        print(f"Error en la transacción: {e}")
    finally:
        session.close() # Siempre cerrar la sesión