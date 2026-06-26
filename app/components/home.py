from reactpy import component, html


@component
def Home():

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
                "placeholder": "Nombre del jugador"
            }
        ),

        html.br(),

        html.br(),

        html.button(
            "Entrar"
        )
    )