from ursina import window, EditorCamera, Ursina
from src.kubek.cube import Cube, Rotation


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

    def input(self, *args):
        super().input(*args)
        self.cube.rotate_cube(Rotation.FRONT_RIGHT)
