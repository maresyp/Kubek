from ursina import window, EditorCamera, Ursina
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

        cube = Cube()
        cube.generate_cubes()
        EditorCamera()
