from reactpy import component, html


@component
def PlayerCard(nombre="Jugador", puntaje=0):

    return html.div(
        {
            "style": {
                "border": "1px solid #CCCCCC",
                "padding": "10px",
                "margin": "8px",
                "borderRadius": "8px",
                "backgroundColor": "#FFFFFF"
            }
        },

        html.h3(f"👤 {nombre}"),

        html.p(f"Puntaje: {puntaje}")
    )