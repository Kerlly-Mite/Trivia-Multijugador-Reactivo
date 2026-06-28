from ConectionSqlCadena import SQLServerConnection

def ejecutar_ejemplo_tradicional():
    # 1. Inicializar la conexión (Modifica con tus datos)
    db = SQLServerConnection(
        server="localhost",
        database="TiendaDB",
        username="sa",
        password="123"
    )
    
    print("--- 1. INSERTAR UN NUEVO PRODUCTO ---")
    query_insert = """
        INSERT INTO Productos (nombre, precio, stock) 
        VALUES (?, ?, ?)
    """
    # Pasamos los datos en una tupla para evitar Inyección SQL
    datos_producto = ("Teclado Mecánico", 89.99, 15)
    
    try:
        db.execute_non_query(query_insert, datos_producto)
    except Exception:
        print("No se pudo insertar el producto.")

    print("\n--- 2. CONSULTAR PRODUCTOS CON BAJO STOCK ---")
    query_select = "SELECT id, nombre, stock FROM Productos WHERE stock < ?"
    limite_stock = (20,) # Las tuplas de un solo elemento llevan coma al final
    
    try:
        resultados = db.execute_query(query_select, limite_stock)
        
        if not resultados:
            print("No hay productos con bajo stock.")
        else:
            print(f"{'ID':<5} | {'Nombre':<25} | {'Stock':<5}")
            print("-" * 40)
            for fila in resultados:
                # Se accede por índice ya que pyodbc devuelve tuplas de fila
                print(f"{fila[0]:<5} | {fila[1]:<25} | {fila[2]:<5}")
                
    except Exception as e:
        print(f"Error al consultar: {e}")
        
    finally:
        # 3. Siempre cerrar la conexión al terminar
        db.close()

if __name__ == "__main__":
    ejecutar_ejemplo_tradicional()