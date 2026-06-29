import asyncio

from types import MappingProxyType

from app.state.game_state import GameState
from app.state.reducer import update
from app.state.actions import START_GAME, END_GAME, NEXT_ROUND

# Estado global único en memoria, compartido por todas las
# sesiones de navegador conectadas al servidor de ReactPy.
state = GameState(
    screen="home",
    players=tuple(),
    current_question=MappingProxyType({}),
    scores=MappingProxyType({}),
    timer=30,
    round_number=1,
    game_started=False,
    game_finished=False
)

# Lista de callbacks (uno por cada pestaña/sesión conectada) que
# se deben notificar cada vez que el estado global cambia, para
# que ReactPy vuelva a renderizar la UI de cada jugador.
subscribers = []


def _disparar_persistencia(accion, estado_anterior, estado_nuevo):
    """
    Lanza las escrituras a base de datos como tareas en segundo
    plano (asyncio.create_task), de forma NO bloqueante: el
    dispatch no espera (no hace await) a que la BD termine de
    escribir antes de devolver el control y notificar a la UI.

    Cualquier problema de conexión/configuración de la BD (driver
    ODBC faltante, servidor apagado, etc.) se reporta en consola
    pero NUNCA debe tumbar el juego ni el dispatch.
    """

    tipo = accion["type"]

    try:

        from app.services import persistence_service

        if tipo == START_GAME:

            asyncio.create_task(
                persistence_service.registrar_inicio_partida()
            )

        elif tipo in (END_GAME, NEXT_ROUND) and estado_nuevo.game_finished:

            asyncio.create_task(
                persistence_service.registrar_resultado_final(
                    estado_nuevo
                )
            )

        elif tipo == "ANSWER_QUESTION":

            asyncio.create_task(
                persistence_service.registrar_evento_historial(
                    id_partida=None,
                    descripcion=(
                        f"{accion.get('jugador')} respondió "
                        f"'{accion.get('opcion')}'"
                    )
                )
            )

    except RuntimeError:

        # No hay event loop corriendo todavía (p. ej. al importar
        # el módulo fuera de la app). En ese caso simplemente no
        # se agenda la tarea de persistencia.
        pass

    except Exception as e:

        # Cualquier otro problema (driver ODBC no instalado, BD
        # apagada, credenciales mal configuradas, etc.) se reporta
        # pero no debe interrumpir el flujo del juego.
        print(f"Persistencia no disponible: {e}")


def dispatch(action):
    """
    Punto único de entrada para modificar el estado global.

    Tanto los clics de los usuarios (desde los componentes) como
    las corrutinas autónomas (timer_task, round_task, events_task)
    deben llamar a esta función en lugar de mutar 'state'
    directamente. Esto garantiza que el estado siempre evolucione
    mediante la función pura update(estado, accion), que todas
    las sesiones conectadas se enteren del cambio, y que los
    eventos relevantes se persistan de forma asíncrona.
    """

    global state

    estado_anterior = state

    nuevo_estado = update(state, action)

    state = nuevo_estado

    _disparar_persistencia(action, estado_anterior, nuevo_estado)

    for callback in list(subscribers):
        callback(nuevo_estado)

    return nuevo_estado
