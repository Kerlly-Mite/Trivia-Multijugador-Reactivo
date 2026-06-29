import time

from database.ConectionSqlCadena import SQLServerConnection


# Ajusta estos datos a tu instancia real de SQL Server.
_db = SQLServerConnection(
    server="JUSTINTG",
    database="TriviaDB",
    username="usu_apvisual",
    password="justin",
    trusted_connection=False
)

_inicio_partida = None


async def registrar_inicio_partida():
    """
    Se llama desde START_GAME (evento del sistema, no solo un
    clic aislado) para marcar el inicio de una partida y poder
    calcular la duración total al finalizar.
    """

    global _inicio_partida

    _inicio_partida = time.monotonic()

    await registrar_evento_historial(
        id_partida=None,
        descripcion="Inicio de partida"
    )


async def registrar_evento_historial(id_partida, descripcion):
    """
    Auditoría temporal de acciones clave: respuestas, cierres
    automáticos de ronda por el sistema, bonus otorgados, etc.
    Se llama tanto desde acciones humanas como desde las
    corrutinas autónomas (timer_task, round_task, events_task).
    """

    query = """
    INSERT INTO HistorialEventos (id_partida, descripcion)
    VALUES (?, ?)
    """

    try:

        await _db.execute_non_query(
            query,
            (id_partida, descripcion)
        )

    except Exception as e:

        print(f"No fue posible registrar el evento: {e}")


async def registrar_resultado_final(estado):
    """
    Se llama cuando el sistema cierra la partida (END_GAME /
    NEXT_ROUND sin más preguntas). Registra ganador, puntaje y
    duración total, y actualiza el ranking global acumulado.
    """

    global _inicio_partida

    jugadores_ordenados = sorted(
        estado.scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    if len(jugadores_ordenados) == 0:
        return

    ganador, puntaje_ganador = jugadores_ordenados[0]

    duracion = 0

    if _inicio_partida is not None:
        duracion = int(time.monotonic() - _inicio_partida)

    query_partida = """
    INSERT INTO Partidas (ganador, puntaje_ganador, duracion_segundos)
    VALUES (?, ?, ?)
    """

    try:

        await _db.execute_non_query(
            query_partida,
            (ganador, puntaje_ganador, duracion)
        )

    except Exception as e:
        print(f"No fue posible registrar la partida: {e}")

    await registrar_evento_historial(
        id_partida=None,
        descripcion=f"Fin de partida. Ganador: {ganador}"
    )

    await actualizar_ranking(jugadores_ordenados)

    _inicio_partida = None


async def actualizar_ranking(jugadores_ordenados):
    """
    Tabla general y persistente de posiciones competitivas.
    Se actualiza automáticamente al cerrar cada partida (evento
    del sistema), no por una acción manual aislada del usuario.
    """

    for posicion, (jugador, puntaje) in enumerate(jugadores_ordenados):

        es_ganador = 1 if posicion == 0 else 0

        query = """
        IF EXISTS (
            SELECT 1 FROM Ranking WHERE jugador = ?
        )
            UPDATE Ranking
            SET puntos_totales = puntos_totales + ?,
                partidas_jugadas = partidas_jugadas + 1,
                victorias = victorias + ?
            WHERE jugador = ?
        ELSE
            INSERT INTO Ranking
                (jugador, puntos_totales, partidas_jugadas, victorias)
            VALUES (?, ?, 1, ?)
        """

        try:

            await _db.execute_non_query(
                query,
                (
                    jugador,
                    puntaje, es_ganador, jugador,
                    jugador, puntaje, es_ganador
                )
            )

        except Exception as e:
            print(f"No fue posible actualizar el ranking de {jugador}: {e}")
