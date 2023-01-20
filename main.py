""" Starting point of application """
from src.kubek.game import Game
from datetime import datetime, date

game = Game()


def main() -> None:
    """ Starting point of application """
    game.run()


def update():
    if game.game_started and game.cube.current_animation.finished:
        if game.cube.check_if_solved():
            game.cube.cube_solved.visible = True
            game.game_started = False
            game.cube.moves.clear()
        else:
            game.cube.cube_solved.visible = False

    if game.game_started:
        duration = datetime.combine(date.min, datetime.time(datetime.now())) - datetime.combine(date.min, game.start_time)
        game.timer.text = f"Czas: {duration}"


if __name__ == "__main__":
    main()
