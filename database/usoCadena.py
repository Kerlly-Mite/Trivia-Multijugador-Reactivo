from ConectionSqlCadena import SQLServerConnection


def ejecutar_ejemplo():

    db = SQLServerConnection(
        server="localhost",
        database="TriviaDB",
        trusted_connection=True
    )

    print("=== INSERTAR EVENTO EN EL HISTORIAL ===")

    query_insert = """
    INSERT INTO HistorialEventos (id_partida, descripcion)
    VALUES (?, ?)
    """

    datos = (
        1,
        "Jugador respondió correctamente la pregunta 3"
    )

    try:
        db.execute_non_query(query_insert, datos)

    except Exception:
        print("No fue posible registrar el evento.")

    print("\n=== CONSULTAR HISTORIAL ===")

    query_select = """
    SELECT
        id_evento,
        id_partida,
        descripcion,
        fecha_hora
    FROM HistorialEventos
    ORDER BY fecha_hora DESC
    """

    try:

        resultados = db.execute_query(query_select)

        for fila in resultados:

            print(
                f"Evento #{fila[0]} | "
                f"Partida {fila[1]} | "
                f"{fila[2]} | "
                f"{fila[3]}"
            )

    except Exception as e:
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    ejecutar_ejemplo()