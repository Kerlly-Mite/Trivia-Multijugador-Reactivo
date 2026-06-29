from reactpy import component, html


@component
def Lobby(estado):

    return html.div(

        html.h2("Sala de Espera"),

        html.h3("Jugadores conectados"),

        html.ul(
            *[
                html.li(f"🟢 {jugador}")
                for jugador in estado.players
            ]
        ) if len(estado.players) > 0 else html.p(
            "Todavía no hay jugadores conectados."
        ),

        html.p("Esperando el inicio de la partida...")
    )
