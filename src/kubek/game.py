"""module containing methods and classes needed to render game"""

from ursina import window, EditorCamera, Ursina, Button, color, Text, Sky
from ursina.input_handler import held_keys
from src.kubek.cube import Cube

from datetime import datetime


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

        self.game_started: bool = False
        self.start_time = datetime.time(datetime.now())
        self.timer = Text(text=f'Czas: 0:00:00', scale=2, x=-.75, y=.38)

        self.solve_button = Button(text='Ułożenie kostki', color=color.azure, scale=(.35, .10), x=-.5, visible=False)
        self.solve_button.on_click = self.cube.backwards_solve

        self.shuffle_button = Button(text='Przetasowanie kostki', color=color.azure, scale=(.35, .10), x=-.5, y=-.11,
                                     visible=False)
        self.shuffle_button.on_click = self.cube.shuffle_cube

        self.start_button = Button(text='Start', color=color.azure, scale=(.35, .10), x=-.5, y=-.22, visible=False)
        self.start_button.on_click = self.start_timer

        self.buttons: list[Button] = []
        self.buttons.append(self.solve_button)
        self.buttons.append(self.shuffle_button)
        self.buttons.append(self.start_button)

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
                    button.disabled = True
                else:
                    button.visible = True
                    button.disabled = False

        if key in Cube.rotations.keys() and self.game_started:
            self.cube.rotate_cube(key, reverse=held_keys["shift"])

    def start_timer(self) -> None:
        self.start_time = datetime.time(datetime.now())
        self.cube.amount_of_moves = 0
        self.cube.moves_counter.text = f'Licznik ruchów: {self.cube.amount_of_moves}'
        self.game_started = True
