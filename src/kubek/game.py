from ursina import Ursina, EditorCamera
from src.kubek.cube import Cube

class Game(Ursina):
    ''' class containging methods needed to render game '''

    def __init__(self) -> None:
        super().__init__()
        EditorCamera()
        self.load_game()

    def load_game(self):
        pass
