from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import text

from SQLServerORM import SQLServerORM, Base


class HistorialEvento(Base):

    __tablename__ = "HistorialEventos"

    id_evento = Column(
        Integer,
        primary_key=True
    )

    id_partida = Column(
        Integer,
        nullable=False
    )

    descripcion = Column(
        String,
        nullable=False
    )

    # SQL Server genera automáticamente la fecha
    fecha_hora = Column(
        DateTime,
        server_default=text("GETDATE()")
    )


def ejecutar_ejemplo():

    orm = SQLServerORM(
        server="localhost",
        database="TriviaDB",
        trusted_connection=True
    )

    session = orm.get_session()

    try:

        print("=== INSERTAR EVENTO CON ORM ===")

        nuevo = HistorialEvento(
            id_partida=1,
            descripcion="Jugador respondió correctamente la pregunta 3"
        )

        session.add(nuevo)
        session.commit()

        # Recargar el objeto desde la BD para obtener la fecha generada
        session.refresh(nuevo)

        print("Evento registrado correctamente.")
        print(f"Fecha asignada por SQL Server: {nuevo.fecha_hora}")

        print("\n=== CONSULTAR HISTORIAL ===")

        eventos = session.query(HistorialEvento).order_by(
            HistorialEvento.id_evento
        ).all()

        for e in eventos:

            print(
                f"Evento #{e.id_evento} | "
                f"Partida {e.id_partida} | "
                f"{e.descripcion} | "
                f"{e.fecha_hora}"
            )

    except Exception as e:

        session.rollback()
        print("Error durante la transacción:", e)

    finally:

        session.close()
        print("\nSesión ORM cerrada.")


if __name__ == "__main__":
    ejecutar_ejemplo()