-- 1. Opcional: Asegúrate de seleccionar tu base de datos antes de ejecutar
-- USE TiendaDB;
-- GO

-- 2. Crear la tabla Productos
CREATE TABLE Productos (
    id INT IDENTITY(1,1) NOT NULL, -- Clave primaria autoincremental (empieza en 1 y aumenta de 1 en 1)
    nombre VARCHAR(100) NOT NULL,  -- Nombre del producto (máximo 100 caracteres, obligatorio)
    precio DECIMAL(10, 2) NOT NULL, -- Precio con hasta 2 decimales (ej: 99999999.99, obligatorio)
    stock INT NOT NULL DEFAULT 0,  -- Cantidad en inventario (entero, obligatorio, por defecto 0)

    -- Definición de la Clave Primaria
    CONSTRAINT PK_Productos PRIMARY KEY CLUSTERED (id)
);
GO

-- 3. Opcional: Insertar algunos datos de prueba iniciales
INSERT INTO Productos (nombre, precio, stock)
VALUES
('Memoria RAM 16GB', 65.00, 25),
('Disco Duro SSD 1TB', 89.99, 5), -- Este saldrá en la consulta de bajo stock (< 20)
('Monitor 24 Pulgadas', 145.50, 12); -- Este también saldrá en bajo stock
GO

