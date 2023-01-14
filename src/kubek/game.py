"""module containing methods and classes needed to render game"""

from ursina import window, EditorCamera, Ursina, Button, color, Text, Sky
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

        self.cube = Cube()
        self.sky = Sky(texture='sky_sunset')

        self.solve_button = Button(text='Solve cube', color=color.azure, scale=(.35, .10), x=-.5, visible=False)
        # self.solve_button.fit_to_text()
        self.solve_button.on_click = self.cube.backwards_solve

        self.shuffle_button = Button(text='Shuffle cube', color=color.azure, scale=(.35, .10), x=-.5, y=-.11, visible=False)
        # self.shuffle_button.fit_to_text()
        self.shuffle_button.on_click = self.cube.shuffle_cube

        self.buttons: list[Button] = []
        self.buttons.append(self.solve_button)
        self.buttons.append(self.shuffle_button)

        self.moves_counter = Text(text='Licznik ruchów: 0', scale=2, x=-.75, y=.48)

        self.camera = EditorCamera()
        self.last_key = None

    def input(self, key, *args):
        super().input(key, *args)

        if key == self.last_key:
            return
        self.last_key = key

        if key == 'escape':
            for button in self.buttons:
                if button.visible:
                    button.visible = False
                else:
                    button.visible = True

        if key in Cube.rotations.keys():
            self.cube.amount_of_moves += 1
            self.moves_counter.text = f"Licznik ruchów {self.cube.get_amount_of_moves()}"
            self.cube.rotate_cube(key, reverse=held_keys["shift"])
