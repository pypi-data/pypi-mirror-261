from docketpy import mathx


def test_square_root():
    assert mathx.square_root(9) == 3


def test_cube_root():
    assert mathx.cube_root(8) == 2


def test_fourth_root():
    assert mathx.fourth_root(16) == 2
