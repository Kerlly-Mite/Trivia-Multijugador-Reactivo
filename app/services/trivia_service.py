QUESTIONS = [

    {
        "question": "Capital del Ecuador",
        "options": ["Quito", "Loja", "Cuenca", "Manta"],
        "correct": "Quito"
    },

    {
        "question": "¿Cuántos colores tiene la bandera de Ecuador?",
        "options": ["2", "3", "4", "5"],
        "correct": "3"
    },

    {
        "question": "¿Cuál es el río más largo del mundo?",
        "options": ["Nilo", "Amazonas", "Mississippi", "Yangtsé"],
        "correct": "Amazonas"
    },

    {
        "question": "¿En qué año se independizó Ecuador de España?",
        "options": ["1809", "1822", "1830", "1845"],
        "correct": "1822"
    },

    {
        "question": "¿Cuál es el animal nacional de Ecuador?",
        "options": ["Cóndor andino", "Jaguar", "Tucán", "Lobo de páramo"],
        "correct": "Cóndor andino"
    }

]


def get_question(indice):

    if indice < 0 or indice >= len(QUESTIONS):
        return None

    return QUESTIONS[indice]


def total_preguntas():

    return len(QUESTIONS)
