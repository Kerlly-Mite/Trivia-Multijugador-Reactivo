from reactpy import component, html

from app.components.player_card import PlayerCard


@component
def Scoreboard(estado):

    jugadores_ordenados = sorted(
        estado.scores.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return html.div(

        html.h2("🏆 Ranking"),

        *[

            PlayerCard(nombre, puntaje)

            for nombre, puntaje in jugadores_ordenados

        ] if len(jugadores_ordenados) > 0 else [
            html.p("Todavía no hay puntajes registrados.")
        ]

    )
