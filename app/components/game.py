from reactpy import component, html

from app.components.question import Question
from app.components.timer import Timer
from app.components.scoreboard import Scoreboard


@component
def Game():

    return html.div(

        html.h2("Trivia Multijugador"),

        Timer(),

        Question(),

        Scoreboard()
    )