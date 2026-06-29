from reactpy import component, html, use_state, use_effect

from app.state import store
from app.state.actions import ANSWER_QUESTION


@component
def Question(estado):

    jugador_activo, set_jugador_activo = use_state(
        estado.players[0] if len(estado.players) > 0 else ""
    )

    respondido, set_respondido = use_state(False)

    opcion_elegida, set_opcion_elegida = use_state(None)

    @use_effect(dependencies=[estado.round_number])
    def reiniciar_al_cambiar_de_ronda():
        # Cada vez que llega una pregunta nueva (round_number
        # cambia), se debe poder volver a responder. Sin este
        # efecto, 'respondido' se queda en True de la ronda
        # anterior y los botones aparecen bloqueados de entrada.
        set_respondido(False)
        set_opcion_elegida(None)

    pregunta = estado.current_question.get(
        "question", "Esperando pregunta..."
    )

    opciones = estado.current_question.get("options", [])

    def manejar_cambio_jugador(evento):
        set_jugador_activo(evento["target"]["value"])
        set_respondido(False)
        set_opcion_elegida(None)

    def responder(opcion):

        def manejador(evento):

            if respondido or jugador_activo == "":
                return

            store.dispatch({
                "type": ANSWER_QUESTION,
                "jugador": jugador_activo,
                "opcion": opcion
            })

            set_opcion_elegida(opcion)
            set_respondido(True)

        return manejador

    respuesta_correcta = estado.current_question.get("correct")

    fue_correcta = (
        respondido and opcion_elegida == respuesta_correcta
    )

    def estilo_boton(opcion):

        if not respondido:
            return {}

        if opcion == respuesta_correcta:
            # Siempre resalta en verde cuál era la correcta,
            # la hayas elegido o no.
            return {
                "backgroundColor": "#4CAF50",
                "color": "white"
            }

        if opcion == opcion_elegida:
            # Esta era la que elegiste y NO era la correcta.
            return {
                "backgroundColor": "#E53935",
                "color": "white"
            }

        return {}

    return html.div(

        html.h2("Pregunta"),

        html.div(
            html.label("Respondiendo como: "),

            html.select(
                {
                    "value": jugador_activo,
                    "on_change": manejar_cambio_jugador
                },
                *[
                    html.option(
                        {"value": jugador},
                        jugador
                    )
                    for jugador in estado.players
                ]
            )
        ),

        html.p(pregunta),

        *[
            html.div(

                html.button(
                    {
                        "on_click": responder(opcion),
                        "disabled": respondido,
                        "style": estilo_boton(opcion)
                    },
                    opcion
                ),

                html.br()

            )

            for opcion in opciones
        ],

        html.p(
            {"style": {"color": "#2E7D32", "fontWeight": "bold"}},
            "✅ ¡Correcto! +10 puntos."
        ) if fue_correcta else (

            html.p(
                {"style": {"color": "#C62828", "fontWeight": "bold"}},
                f"❌ Incorrecto. La respuesta era: {respuesta_correcta}"
            ) if respondido else None
        )
    )