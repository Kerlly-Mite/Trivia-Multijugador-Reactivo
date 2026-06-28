from reactpy import component, html

from app.components.player_card import PlayerCard


@component
def Scoreboard(jugadores=None):

    if jugadores is None:

        jugadores = [

            ("Katherine",120),

            ("Carlos",90),

            ("María",75)

        ]

    return html.div(

        html.h2("🏆 Ranking"),

        *[

            PlayerCard(nombre,puntaje)

            for nombre,puntaje in jugadores

        ]

    )