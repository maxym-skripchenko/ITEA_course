import sys
from hw.files_hw import rec



def test_func1():
    assert rec('aba', 'aba') == 'aba and aba'


def test_func2():
    assert open('/Users/nicktrynus/ITEA/ITEA_course/Nikita_Trynus/8_files/hw/semordnilap.txt', 'r')


def test_func3():
    assert rec('aba','abb')==None
