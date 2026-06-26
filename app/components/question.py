from reactpy import component, html


@component
def Question():

    return html.div(

        html.h2("Pregunta"),

        html.p("¿Cuál es la capital del Ecuador?"),

        html.button("Quito"),

        html.br(),

        html.button("Guayaquil"),

        html.br(),

        html.button("Cuenca"),

        html.br(),

        html.button("Loja")
    )