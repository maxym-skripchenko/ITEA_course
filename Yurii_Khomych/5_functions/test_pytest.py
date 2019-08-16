from practise.ex1 import my_max

def test_practise_ex_1_max():
    assert my_max([1,2,3]) == 3

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"


def test_sum_tuple():
    assert sum((2, 2, 2)) == 6, "Should be 6"
