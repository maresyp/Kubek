""" Starting point of application """
from src.kubek.game import Game

game = Game()


def main() -> None:
    """ Starting point of application """
    game.run()


def update():
    if game.cube.amount_of_moves != 0 and game.cube.current_animation.finished:
        game.cube.check_if_solved()


if __name__ == "__main__":
    main()
