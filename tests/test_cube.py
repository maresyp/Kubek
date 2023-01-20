import pytest

from src.kubek.cube import Cube


def test_cube_rotation() -> None:
    """Test rotation of cube"""
    with pytest.raises(ValueError):
        cube: Cube = Cube()
