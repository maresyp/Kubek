""" Module containing classes and methods to perform actions on cube """
from enum import Enum, auto
from typing import Self
from ursina import Entity, color, Vec3
import random


class Colors(Enum):
    """Enumeration containing colors for cube"""

    GREEN = color.rgb(0, 153, 0)
    RED = color.rgb(153, 0, 0)
    BLUE = color.rgb(51, 204, 255)


class Rotation(Enum):
    """Enumeration containing expected values for cube rotation"""

    # TODO: add everything
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Cube:
    """3D cube object"""

    def __init__(self) -> None:
        pass

    def generate_cube(self) -> None:
        """Actions needed to generate cube"""
        entities: list[Entity] = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    entities.append(
                        Entity(
                            position=Vec3(i, j, k),
                            model="cube",
                            texture="white_cube",
                        )
                    )

        for cube in entities:
            cube.color = random.choice(
                [Colors.RED.value, Colors.GREEN.value, Colors.BLUE.value]
            )

    def rotate_cube(self, direction: Rotation, amount_of_rotations: int = 1) -> Self:
        if amount_of_rotations <= 0:
            raise ValueError("Number of rotations can't be less than 0")

        for _ in range(amount_of_rotations):
            match direction:
                case Rotation.LEFT:
                    pass
                case _:
                    raise ValueError(f"Illegal direction {direction}")
            # rotate depending on direction

        return self
