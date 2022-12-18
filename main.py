""" Starting point of application """
from src.kubek.game import Game


def main() -> None:
    """ Starting point of application """
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
