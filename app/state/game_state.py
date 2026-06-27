from dataclasses import dataclass


@dataclass(frozen=True)
class GameState:

    screen: str

    players: list

    current_question: dict

    scores: dict

    timer: int

    round_number: int

    game_started: bool

    game_finished: bool