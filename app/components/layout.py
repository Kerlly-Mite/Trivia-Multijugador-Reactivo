from reactpy import component, html, use_state, use_effect

from app.state.store import state as estado_global
from app.components.home import Home
from app.components.lobby import Lobby
from app.components.game import Game
from app.components.results import Results


@component
def Layout():

    estado, set_estado = use_state(estado_global)

    def on_estado_cambio(nuevo_estado):
        set_estado(nuevo_estado)

    @use_effect(dependencies=[])
    def suscribirse():

        from app.state import store

        store.subscribers.append(on_estado_cambio)

        def desuscribirse():
            if on_estado_cambio in store.subscribers:
                store.subscribers.remove(on_estado_cambio)

        return desuscribirse

    if estado.screen == "home":
        pantalla = Home(estado)

    elif estado.screen == "lobby":
        pantalla = Lobby(estado)

    elif estado.screen == "game":
        pantalla = Game(estado)

    elif estado.screen == "results":
        pantalla = Results(estado)

    else:
        pantalla = Home(estado)

    return html.div(
        {
            "style": {
                "width": "800px",
                "margin": "40px auto",
                "padding": "20px",
                "border": "2px solid #1E88E5",
                "borderRadius": "10px",
                "fontFamily": "Arial",
                "textAlign": "center",
                "backgroundColor": "#F5F5F5"
            }
        },

        html.h1(
            "Trivia Multijugador Reactivo"
        ),

        html.hr(),

        pantalla
    )
