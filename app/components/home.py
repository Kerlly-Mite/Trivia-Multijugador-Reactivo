from reactpy import component, html, use_state

from app.state import store
from app.state.actions import ENTER_PLAYER, START_GAME


@component
def Home(estado):

    nombre, set_nombre = use_state("")
    error, set_error = use_state("")

    def manejar_cambio_nombre(evento):
        set_nombre(evento["target"]["value"])
        set_error("")

    def manejar_click_entrar(evento):

        nombre_limpio = nombre.strip()

        if nombre_limpio == "":
            set_error("Debes ingresar un nombre.")
            return

        store.dispatch({
            "type": ENTER_PLAYER,
            "nombre": nombre_limpio
        })

        set_nombre("")

    return html.div(

        html.h2(
            "Inicio"
        ),

        html.p(
            "Ingrese su nombre para comenzar."
        ),

        html.input(
            {
                "type": "text",
                "placeholder": "Nombre del jugador",
                "value": nombre,
                "on_change": manejar_cambio_nombre
            }
        ),

        html.br(),

        html.br(),

        html.button(
            {
                "on_click": manejar_click_entrar
            },
            "Entrar"
        ),

        html.p(
            {
                "style": {"color": "red"}
            },
            error
        ) if error else None,

        html.hr(),

        html.h3(f"Jugadores en sala: {len(estado.players)}"),

        html.ul(
            *[
                html.li(f"🟢 {jugador}")
                for jugador in estado.players
            ]
        ),

        html.button(
            {
                "on_click": lambda evento: store.dispatch(
                    {"type": START_GAME}
                ),
                "disabled": len(estado.players) == 0
            },
            "Iniciar partida"
        ) if len(estado.players) > 0 else None
    )
