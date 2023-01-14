""" Module containing classes and methods to perform actions on cube """
from typing import Self
from itertools import product
import random

from ursina import Entity, scene, Sequence, Func
from ursina.ursinastuff import invoke


class IncorrectRotation(Exception):
    """Exception indicating that rotation is incorrect"""


class Cube:
    """3D cube object"""

    # Possible cube rotations - https://ruwix.com/the-rubiks-cube/notation/
    rotations: dict[str, list[str, int, int]] = {
        "u": ["y", 1, 90],
        "e": ["y", 0, -90],
        "d": ["y", -1, -90],
        "l": ["x", -1, -90],
        "m": ["x", 0, -90],
        "r": ["x", 1, 90],
        "f": ["z", -1, 90],
        "s": ["z", 0, 90],
        "b": ["z", 1, -90],
    }

    def __init__(self) -> None:
        self.entities: list[Entity] = []
        self.center: Entity = Entity()
        self.current_animation: Sequence = Sequence()
        self.moves: list[tuple[str, bool]] = []
        self.amount_of_moves: int = 0
        self.__generate_cubes()

    def get_amount_of_moves(self) -> int:
        return self.amount_of_moves

    def __generate_cubes(self) -> None:
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

    def __find_relative_cubes(self, axis, layer) -> None:
        for entity in self.entities:
            # assign global positions of cubes to their local position so they will stay in place
            entity.rotation = entity.world_rotation
            entity.position = round(entity.world_position, 1)
            entity.parent = scene

        # reset center position
        self.center.rotation = 0

        # find cubes that are relative to center and are needed to rotate
        for entity in self.entities:
            match axis:
                case "x":
                    if entity.position.x == layer:
                        entity.parent = self.center
                case "y":
                    if entity.position.y == layer:
                        entity.parent = self.center
                case "z":
                    if entity.position.z == layer:
                        entity.parent = self.center
                case _:
                    raise ValueError(f"{axis} is not correct value")

    def rotate_cube(
        self,
        direction: str,
        reverse: bool = False,
        amount_of_rotations: int = 1,
        rotation_duration: float = 0.5,
        save_moves=True,
    ) -> Self:  # type: ignore
        """Function responsible for rotation of cube"""
        if amount_of_rotations <= 0:
            raise ValueError("Number of rotations can't be less than 0")

        if not self.current_animation.finished:
            return self

        for _ in range(amount_of_rotations):
            if save_moves:
                self.moves.append((direction, reverse))
            axis, layer, angle = self.rotations[direction]
            self.__find_relative_cubes(axis=axis, layer=layer)
            angle = -1 * angle if reverse else angle

            match axis:
                case "x":
                    self.current_animation = self.center.animate_rotation_x(
                        angle, duration=rotation_duration
                    )
                case "y":
                    self.current_animation = self.center.animate_rotation_y(
                        angle, duration=rotation_duration
                    )
                case "z":
                    self.current_animation = self.center.animate_rotation_z(
                        angle, duration=rotation_duration
                    )
                case _:
                    raise ValueError(f"{axis} is not correct value")

        return self

    def shuffle_cube(
        self, rotations: int = 25, rotation_duration: float = 0.25
    ) -> Self:  # type: ignore
        """Method used to shuffle cube before playing"""
        if rotations <= 0:
            raise ValueError("Amount of rotations can't be less than 0")

        self.amount_of_moves = 0

        for delay in [(x * (rotation_duration + 0.1)) for x in range(rotations)]:
            invoke(
                Func(
                    self.rotate_cube,
                    random.choice(list(Cube.rotations.keys())),
                    rotation_duration=rotation_duration,
                ),
                delay=delay,
            )

        return self

    def backwards_solve(self, rotation_duration: float = 0.25) -> Self:  # type: ignore
        """Solving cube by doing every move but backwards"""

        self.amount_of_moves = 0

        for delay in [(x * (rotation_duration + 0.1)) for x in range(len(self.moves))]:
            direction, reverse = self.moves.pop()
            invoke(
                Func(
                    self.rotate_cube,
                    direction,
                    reverse=not reverse,
                    save_moves=False,
                    rotation_duration=rotation_duration,
                ),
                delay=delay,
            )

        return self
