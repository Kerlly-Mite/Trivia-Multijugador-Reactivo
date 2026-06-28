from reactpy import component, html

from app.components.layout import Layout
from app.components.timer import Timer
from app.components.question import Question
from app.components.scoreboard import Scoreboard


@component
def Game():

    return html.div(

        Layout(),

        html.br(),

        Timer(),

        html.hr(),

        Question(),

        html.hr(),

        Scoreboard()

    )