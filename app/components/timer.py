from reactpy import component, html


@component
def Timer(segundos=30):

    return html.div(

        html.h3("⏳ Tiempo restante"),

        html.h1(f"{segundos} s")
    )