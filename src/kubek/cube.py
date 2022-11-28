""" Module containing classes and methods to perform actions on cube """
from enum import Enum, auto
from typing import Literal, Self


class Colors(Enum):
    """ Enumeration containing colors for cube """
    GREEN = ()
    RED = ()
    BLUE = ()


class Rotation(Enum):
    """ Enumeration containing expected values for cube rotation """
    # TODO: add everything
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()


class Cube:
    """ 3D cube object """

    def __init__(self) -> None:
        pass

    def rotate_cube(self, direction: int, amount_of_rotations: int = 1) -> Self:
        if amount_of_rotations <= 0:
            raise ValueError("Number of rotations can't be less than 0")

        for _ in range(amount_of_rotations):
            match direction:
                case Rotation.LEFT:
                    pass
                case _:
                    raise ValueError(f'Illegal direction {direction}')
            # rotate depending on direction

        return self

