from dataclasses import dataclass, field
from types import MappingProxyType


@dataclass(frozen=True)
class GameState:

    screen: str

    players: tuple

    current_question: MappingProxyType

    scores: MappingProxyType

    timer: int

    round_number: int

    game_started: bool

    game_finished: bool
