import sys

from hw.hw_func import make_3sg_form, make_ing_form, make_ing_form


def test_1():
    assert make_3sg_form('try') == 'tries'


def test_2():
    assert make_ing_form('lie') == 'lying'


def test_3():
    assert  make_ing_form('run') == 'running'
