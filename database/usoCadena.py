from ConectionSqlCadena import SQLServerConnection


def ejecutar_ejemplo_tradicional():

    # Crear conexión
    db = SQLServerConnection(
        server="localhost",
        database="TriviaDB",
        username="sa",
        password="123456"
    )

    print("=== INSERTAR EVENTO EN EL HISTORIAL ===")

    query_insert = """
        INSERT INTO HistorialEventos
        (jugador, evento)
        VALUES (?, ?)
    """

    datos = (
        "Maria",
        "Ingreso a la sala de espera"
    )

    try:
        db.execute_non_query(
            query_insert,
            datos
        )

    except Exception:
        print("No fue posible registrar el evento.")

    print("\n=== CONSULTAR HISTORIAL ===")

    query_select = """
        SELECT id, jugador, evento, fecha
        FROM HistorialEventos
    """

    try:

        resultados = db.execute_query(
            query_select
        )

        if not resultados:
            print("No existen eventos registrados.")

        else:

            print(
                f"{'ID':<5} "
                f"{'Jugador':<15} "
                f"{'Evento':<35} "
                f"{'Fecha'}"
            )

            print("-" * 80)

            for fila in resultados:

                print(
                    f"{fila[0]:<5} "
                    f"{fila[1]:<15} "
                    f"{fila[2]:<35} "
                    f"{fila[3]}"
                )

    except Exception as e:
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    ejecutar_ejemplo_tradicional()