from reactpy import component, html


@component
def Question(
    pregunta="¿Cuál es la capital del Ecuador?",
    opciones=None
):

    if opciones is None:

        opciones = [

            "Quito",

            "Guayaquil",

            "Cuenca",

            "Loja"

        ]

    return html.div(

        html.h2("Pregunta"),

        html.p(pregunta),

        *[
            html.div(

                html.button(opcion),

                html.br()

            )

            for opcion in opciones
        ]
    )