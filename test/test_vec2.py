"""Template test module."""
from typing import Tuple

import pytest
from virtual_joystick.utils import Vec2


@pytest.fixture(name="xy")
def fixture_xy() -> Tuple[float]:
    return (0.34, -0.98)


@pytest.fixture(name="xy_clip")
def fixture_xy_clip() -> float:
    return (1.3, -4.98)


class TestVec2:
    """Test class."""

    def test_default(self) -> None:
        vec = Vec2()
        assert vec.x == pytest.approx(0.0)
        assert vec.y == pytest.approx(0.0)

    def test_vals(self, xy) -> None:
        vec = Vec2(xy[0], xy[1])
        assert vec.x == pytest.approx(xy[0])
        assert vec.y == pytest.approx(xy[1])

    def test_clip(self, xy_clip) -> None:
        vec = Vec2(xy_clip[0], xy_clip[1])
        assert vec.x == pytest.approx(min(max(-1.0, xy_clip[0]), 1.0))
        assert vec.y == pytest.approx(min(max(-1.0, xy_clip[1]), 1.0))
