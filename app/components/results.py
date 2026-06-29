from reactpy import component, html

from app.state import store
from app.state.actions import RESET_GAME


@component
def Results(estado):

    jugadores_ordenados = sorted(
        estado.scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    ganador = jugadores_ordenados[0] if jugadores_ordenados else None

    def volver_al_inicio(evento):

        store.dispatch({"type": RESET_GAME})

    return html.div(

        html.h2("🏆 Resultados"),

        html.h3("Ganador"),

        html.h1(ganador[0] if ganador else "Sin ganador"),

        html.h3("Puntajes"),

        html.ul(
            *[
                html.li(f"{nombre} - {puntaje}")
                for nombre, puntaje in jugadores_ordenados
            ]
        ),

        html.button(
            {
                "on_click": volver_al_inicio
            },
            "Volver al inicio"
        )
    )
