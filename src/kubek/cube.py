""" Module containing classes and methods to perform actions on cube """
from enum import Enum, auto
from typing import Self
from itertools import product

from ursina import Entity, Vec3, color, load_texture


class Colors(Enum):
    """Enumeration containing colors for cube"""

    GREEN = color.rgb(0, 153, 0)
    RED = color.rgb(153, 0, 0)
    BLUE = color.rgb(51, 204, 255)


class Rotation(Enum):
    """Enumeration containing expected values for cube rotation"""

    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Cube:
    """3D cube object"""

    def __init__(self) -> None:
        self.entities: list[Entity] = []
        self.center = Entity()

    def generate_cubes(self) -> None:
        """Actions needed to generate cube"""

        for pos in product((-1, 0, 1), repeat=3):
            self.entities.append(
                Entity(
                    position=pos,
                    model="model.obj",
                    texture="texture.png",
                    scale=0.5,
                )
            )

    def rotate_cube(self, direction: Rotation, amount_of_rotations: int = 1) -> Self:
        if amount_of_rotations <= 0:
            raise ValueError("Number of rotations can't be less than 0")

        for _ in range(amount_of_rotations):
            match direction:
                case Rotation.LEFT:
                    ...
                case _:
                    raise ValueError(f"Illegal direction {direction}")

        return self
