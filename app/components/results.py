from reactpy import component, html


@component
def Results():

    return html.div(

        html.h2("🏆 Resultados"),

        html.h3("Ganador"),

        html.h1("Katherine"),

        html.h3("Puntajes"),

        html.ul(

            html.li("Katherine - 120"),

            html.li("Carlos - 90"),

            html.li("María - 75")
        ),

        html.button("Volver al inicio")
    )