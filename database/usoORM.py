from sqlalchemy import Column, Integer, String
from SQLServerORM import SQLServerORM, Base


# Modelo que representa la tabla HistorialEventos
class HistorialEvento(Base):

    __tablename__ = "HistorialEventos"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    jugador = Column(
        String(50),
        nullable=False
    )

    evento = Column(
        String(255),
        nullable=False
    )


def ejecutar_ejemplo_orm():

    orm = SQLServerORM(
        server="localhost",
        database="TriviaDB",
        username="sa",
        password="123456"
    )

    session = orm.get_session()

    try:

        print("=== INSERTAR EVENTO CON ORM ===")

        nuevo_evento = HistorialEvento(
            jugador="Kerlly",
            evento="Respondió correctamente la pregunta 3"
        )

        session.add(
            nuevo_evento
        )

        session.commit()

        print(
            f"Evento registrado correctamente. "
            f"ID asignado: {nuevo_evento.id}"
        )

        print("\n=== CONSULTAR HISTORIAL ===")

        historial = session.query(
            HistorialEvento
        ).all()

        for evento in historial:

            print(
                f"[{evento.id}] "
                f"{evento.jugador} -> "
                f"{evento.evento}"
            )

    except Exception as e:

        session.rollback()

        print(
            f"Error durante la transacción: {e}"
        )

    finally:

        session.close()

        print(
            "\nSesión ORM cerrada."
        )


if __name__ == "__main__":
    ejecutar_ejemplo_orm()