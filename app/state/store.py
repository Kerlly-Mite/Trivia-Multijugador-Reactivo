from app.state.game_state import GameState

state = GameState(
    screen="home",
    players=[],
    current_question={},
    scores={},
    timer=30,
    round_number=1,
    game_started=False,
    game_finished=False
)