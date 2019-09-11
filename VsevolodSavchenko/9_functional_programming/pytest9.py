from hw.hw1 import make_3sg_form
from hw.hw2 import make_ing_form

def test_hw1_make_3sg_form():
    assert make_3sg_form("go") == "goes"

def test_hw2_make_ing_form():
    assert make_ing_form("go") == "going"