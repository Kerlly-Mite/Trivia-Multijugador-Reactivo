from reactpy import component, html


@component
def Lobby():

    return html.div(

        html.h2("Sala de Espera"),

        html.h3("Jugadores conectados"),

        html.ul(

            html.li("🟢 Katherine"),

            html.li("🟢 Carlos"),

            html.li("🟢 María")
        ),

        html.p("Esperando el inicio de la partida...")
    )