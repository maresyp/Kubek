""" Module containing classes and methods to perform actions on cube """
from enum import Enum
from typing import Self
from itertools import product

from ursina import Entity, scene


class IncorrectRotation(Exception):
    """Exception indicating that rotation is incorrect"""


class Rotation(Enum):
    """Enumeration containing expected values for cube rotation"""

    FRONT_RIGHT = "f"


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
        self.center = Entity()
        self.current_animation = None
        self.__generate_cubes()

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

    def __snap_cube_to_closest_rotation(self, cube: Entity):
        # find closest possible rotation
        print(f"Before : {cube.world_rotation=}, {cube.world_position=}")
        allowed_angles: list[int] = [-180, -90, 0, 90, 180]

        x_min = min(allowed_angles, key=lambda x: abs(x - int(cube.world_rotation_x)))
        x_diff: float = cube.world_rotation_x - x_min
        if x_diff > 2.0:
            raise IncorrectRotation(f"{x_diff}")

        y_min = min(allowed_angles, key=lambda x: abs(x - int(cube.world_rotation_y)))
        y_diff: float = cube.world_rotation_y - y_min
        if y_diff > 2.0:
            raise IncorrectRotation(f"{y_diff}")

        z_min = min(allowed_angles, key=lambda x: abs(x - int(cube.world_rotation_z)))
        z_diff: float = cube.world_rotation_z - z_min
        if z_diff > 2.0:
            raise IncorrectRotation(f"{z_diff}")

        cube.world_rotation.x = x_min
        cube.world_rotation.y = y_min
        cube.world_rotation.z = z_min

        print(f"{x_diff=}, {y_diff=}, {z_diff=}")

    def __find_relative_cubes(self, axis, layer) -> None:
        for entity in self.entities:
            self.__snap_cube_to_closest_rotation(entity)  # TODO : bug tutaj napaw
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
        self, direction: str, reverse: bool = False, amount_of_rotations: int = 1
    ) -> Self:
        if amount_of_rotations <= 0:
            raise ValueError("Number of rotations can't be less than 0")

        if self.current_animation is not None:
            if not self.current_animation.finished:
                return self

        for _ in range(amount_of_rotations):
            axis, layer, angle = self.rotations[direction]
            try:
                self.__find_relative_cubes(axis=axis, layer=layer)
                angle = -1 * angle if reverse else angle

                match axis:
                    case "x":
                        self.current_animation = self.center.animate_rotation_x(angle, duration=0.5)
                    case "y":
                        self.current_animation = self.center.animate_rotation_y(angle, duration=0.5)
                    case "z":
                        self.current_animation = self.center.animate_rotation_z(angle, duration=0.5)
                    case _:
                        raise ValueError(f"{axis} is not correct value")
            except IncorrectRotation as exception:
                print(f"IncorrectRotation {exception}")

        return self
