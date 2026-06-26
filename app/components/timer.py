from reactpy import component, html


@component
def Timer():

    return html.div(

        html.h3("⏳ Tiempo restante"),

        html.h1("30 s")
    )