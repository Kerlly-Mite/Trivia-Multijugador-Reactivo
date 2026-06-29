from reactpy import component, html


@component
def Timer(estado):

    return html.div(

        html.h3("⏳ Tiempo restante"),

        html.h1(f"{estado.timer} s")
    )
