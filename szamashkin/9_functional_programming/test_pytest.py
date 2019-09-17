from hw.hw1 import make_3sg_form
from hw.hw2 import make_ing_form


def test_make_3sg_form():
    assert make_3sg_form("brush") == "brushes", "Should be brushes"


def test_make_ing_form():
    assert make_ing_form("see") == "seeing", "Should be seeing"
