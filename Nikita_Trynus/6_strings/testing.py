import sys
sys.path.append(r'/Users/nicktrynus/ITEA/ITEA_course/Nikita_Trynus/6_strings/hw')
import hw_6


def test_func1():
    assert hw_6.map_str_to_int(['1', '22', '333']) == [1,2,3]


def test_func2():
    assert hw_6.find_longest_word(['1', '22', '333']) == 3


def test_func3():
    assert hw_6.filter_long_words(['1', '22', '333'], 2) == ['22', '333']

