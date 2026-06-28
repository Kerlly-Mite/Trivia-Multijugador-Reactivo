from sqlalchemy import Column, Integer, String, Float
from SQLServerORM import SQLServerORM, Base

# 1. Definimos el Modelo que mapea exactamente a la tabla de la BD
class Producto(Base):
    __tablename__ = 'Productos'  # Nombre real de la tabla en SQL Server
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

def ejecutar_ejemplo_orm():
    # 2. Inicializar el ORM
    orm = SQLServerORM(
        server="localhost",
        database="TiendaDB",
        username="sa",
        password="anthony23"
    )
    
    # 3. Abrir una sesión
    session = orm.get_session()
    
    try:
        print("--- 1. INSERTAR UN NUEVO PRODUCTO CON ORM ---")
        # Creamos el producto como un objeto de Python normal
        nuevo_producto = Producto(nombre="Mouse Gamer", precio=45.50, stock=8)
        
        session.add(nuevo_producto)  # Lo preparamos para la BD
        session.commit()             # Confirmamos la transacción
        print(f"Producto insertado con éxito. ID asignado: {nuevo_producto.id}")
        
        print("\n--- 2. CONSULTAR Y ACTUALIZAR CON ORM ---")
        # Buscamos el producto que acabamos de crear usando su nombre
        producto_bd = session.query(Producto).filter(Producto.nombre == "Mouse Gamer").first()
        
        if producto_bd:
            print(f"Encontrado: {producto_bd.nombre} - Stock actual: {producto_bd.stock}")
            
            # Modificar el stock es tan fácil como cambiar la propiedad del objeto
            print("Modificando stock...")
            producto_bd.stock = 25 
            session.commit() # SQLAlchemy detecta el cambio y hace el UPDATE por ti
            print("¡Stock actualizado en la base de datos!")

        print("\n--- 3. LISTAR TODOS LOS PRODUCTOS ---")
        todos_los_productos = session.query(Producto).all()
        for prod in todos_los_productos:
            # Accedemos a los campos como propiedades del objeto
            print(f"[{prod.id}] {prod.nombre} - ${prod.precio} (Stock: {prod.stock})")

    except Exception as e:
        session.rollback()  # Si algo falla, deshacemos los cambios
        print(f"Ocurrió un error en el ORM: {e}")
        
    finally:
        # 4. Siempre cerrar la sesión para liberar conexiones al pool
        session.close()
        print("\nSesión ORM cerrada.")

if __name__ == "__main__":
    ejecutar_ejemplo_orm()