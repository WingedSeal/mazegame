from ..game import Game


game: Game | None = None


def get_game() -> Game:
    if game is None:
        raise ValueError(
            "You tried to run script directly! The game was never set up! Try 'run(script)' instead."
        )
    return game
