"""Template test module."""
import pytest
from virtual_joystick.utils import Vec2
# import the internal libs and test


class TestVec2:
    """Test class."""

    @pytest.mark.parametrize("x,y", (1.3, -0.98))
    def test_default(self) -> None:
        vec = Vec2()
        assert vec.x == vec.y == 0.0

    def test_vals(self, x, y) -> None:
        vec = Vec2.add(x, y)
        assert vec.x == x
        assert vec.y == y
