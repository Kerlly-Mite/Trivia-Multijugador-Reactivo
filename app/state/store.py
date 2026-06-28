from app.state.reducer import update, GameState

# estado global del juego
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