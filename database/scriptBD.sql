-- ==========================================
-- BASE DE DATOS: Trivia Multijugador Reactivo
-- ==========================================

-- Crear tabla de partidas
CREATE TABLE Partidas (
    id_partida INT IDENTITY(1,1) PRIMARY KEY,
    ganador VARCHAR(50),
    puntaje_ganador INT,
    duracion_segundos INT,
    fecha DATETIME DEFAULT GETDATE()
);
GO


-- Crear tabla de historial de eventos
CREATE TABLE HistorialEventos (
    id_evento INT IDENTITY(1,1) PRIMARY KEY,
    id_partida INT,
    descripcion VARCHAR(255),
    fecha_hora DATETIME DEFAULT GETDATE(),

    CONSTRAINT FK_Historial_Partidas
        FOREIGN KEY (id_partida)
        REFERENCES Partidas(id_partida)
);
GO


-- Crear tabla de ranking global
CREATE TABLE Ranking (
    id_ranking INT IDENTITY(1,1) PRIMARY KEY,
    jugador VARCHAR(50) NOT NULL,
    puntos_totales INT DEFAULT 0,
    partidas_jugadas INT DEFAULT 0,
    victorias INT DEFAULT 0
);
GO


-- Datos de prueba
INSERT INTO Ranking
(jugador, puntos_totales, partidas_jugadas, victorias)
VALUES
('Ana',120,5,3),
('Luis',90,4,2),
('Carlos',150,6,4);
GO