"""module containing methods and classes needed to render game"""

from ursina import window, EditorCamera, Ursina
from ursina.input_handler import held_keys
from src.kubek.cube import Cube


class Game(Ursina):
    """class containing methods needed to render game"""

    def __init__(self) -> None:
        super().__init__()

        # setup things related to window
        window.title = "Kubek"
        window.borderless = False
        window.fps_counter.enabled = True
        window.exit_button.visible = False

        self.camera = EditorCamera()
        self.cube = Cube()
        self.last_key = None

    def input(self, key, *args):
        super().input(key, *args)

        if key == self.last_key:
            return

        self.last_key = key
        if key == 'x':
            self.cube.shuffle_cube()

        if key == 'z':
            self.cube.backwards_solve()

        if key in Cube.rotations.keys():
            self.cube.rotate_cube(key, reverse=held_keys["shift"])
