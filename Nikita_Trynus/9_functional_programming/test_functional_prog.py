import sys
sys.path.append(r'/Users/nicktrynus/ITEA/ITEA_course/Nikita_Trynus/9_functional_programming/hw')
import hw_func


def test_1():
    assert hw_func.make_3sg_form('try') == 'tries'


def test_2():
    assert hw_func.make_ing_form('lie') == 'lying'


def test_3():
    assert  hw_func.make_ing_form('run') == 'running'
