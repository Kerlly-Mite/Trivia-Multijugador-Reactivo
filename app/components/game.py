from reactpy import component, html

from app.components.timer import Timer
from app.components.question import Question
from app.components.scoreboard import Scoreboard


@component
def Game(estado):

    return html.div(

        html.h2(f"Ronda {estado.round_number}"),

        Timer(estado),

        html.hr(),

        Question(estado),

        html.hr(),

        Scoreboard(estado)

    )
