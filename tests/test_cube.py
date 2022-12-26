import pytest

from src.kubek.cube import Cube
from src.kubek.cube import Rotation


def test_cube_rotation() -> None:
    """Test rotation of cube"""
    with pytest.raises(ValueError):
        cube: Cube = Cube()
        cube.rotate_cube(Rotation.LEFT, 0)
        cube.rotate_cube(Rotation.RIGHT, -1)
