from reactpy import component, html


@component
def Layout():

    return html.div(
        {
            "style": {
                "width": "800px",
                "margin": "40px auto",
                "padding": "20px",
                "border": "2px solid #1E88E5",
                "borderRadius": "10px",
                "fontFamily": "Arial",
                "textAlign": "center",
                "backgroundColor": "#F5F5F5"
            }
        },

        html.h1(
            "🎮 Trivia Multijugador Reactivo"
        ),

        html.hr(),

        html.p(
            "Bienvenido al sistema de Trivia."
        )
    )