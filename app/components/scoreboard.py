from reactpy import component, html
from app.components.player_card import PlayerCard


@component
def Scoreboard():

    return html.div(

        html.h2("🏆 Ranking"),

        PlayerCard("Katherine", 120),

        PlayerCard("Carlos", 90),

        PlayerCard("María", 75)
    )