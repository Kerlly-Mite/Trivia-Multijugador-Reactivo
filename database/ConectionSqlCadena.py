import pyodbc

class SQLServerConnection:
    def __init__(self, server, database, username=None, password=None, trusted_connection=False):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.trusted_connection = trusted_connection
        self.conn = None

    def _build_connection_string(self):
        # Driver estándar para SQL Server (asegúrate de tenerlo instalado en tu OS)
        driver = "{ODBC Driver 17 for SQL Server}"
        
        if self.trusted_connection:
            # Autenticación de Windows
            return f"DRIVER={driver};SERVER={self.server};DATABASE={self.database};Trusted_Connection=yes;"
        else:
            # Autenticación de SQL Server (Usuario y Contraseña)
            return f"DRIVER={driver};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};"

    def connect(self):
        """Establece la conexión con la base de datos."""
        try:
            conn_str = self._build_connection_string()
            self.conn = pyodbc.connect(conn_str)
            print("¡Conexión exitosa a SQL Server!")
            return self.conn
        except Exception as e:
            print(self._error_message("conectar", e))
            raise

    def execute_query(self, query, params=None):
        """Ejecuta una consulta (SELECT) y devuelve los resultados."""
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
            print(self._error_message("ejecutar consulta", e))
            raise

    def execute_non_query(self, query, params=None):
        """Ejecuta comandos que cambian datos (INSERT, UPDATE, DELETE)."""
        if not self.conn:
            self.connect()
            
        try:
            with self.conn.cursor() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.conn.commit()  # Guarda los cambios
                print("Operación realizada con éxito.")
        except Exception as e:
            if self.conn:
                self.conn.rollback()  # Revierte cambios si hay error
            print(self._error_message("ejecutar comando", e))
            raise

    def close(self):
        """Cierra la conexión."""
        if self.conn:
            self.conn.close()
            print("Conexión cerrada.")

    def _error_message(self, action, error):
        return f"❌ Error al {action} en SQL Server: {error}"

# --- MODO DE USO ---
if __name__ == "__main__":
    # Ejemplo con Autenticación de SQL Server
    db = SQLServerConnection(
        server="TU_SERVIDOR_O_IP",
        database="TuBaseDeDatos",
        username="sa",
        password="TuPasswordSeguro"
    )
    
    # Ejemplo de SELECT
    usuarios = db.execute_query("SELECT id, nombre FROM Usuarios WHERE activo = ?", (1,))
    for usuario in usuarios:
        print(usuario.nombre)
        
    db.close()