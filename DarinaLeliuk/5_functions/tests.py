import unittest

def test_practise_1():
    assert my_max(2, 4) == 4, "Should be 4"

def test_practise_2():
    assert my_len(function) == 8, "Should be 8"

def test_practise_3():
    assert vowel_or_not("o") == True, "Should be True"

def test_practise_4():
    assert my_multiple([1, 1, 1]) == 1, "Should be 1"
    assert my_sum([1, 1, 1]) == 3, "Should be 3"

def test_practise_5():
    assert is_member(10, [1, 6, 9, 10]) == True, "Should be True"

def test_practise_6():
    assert overlapping([1, 2, 3], [2, 5, 6]) == True, "Should be True"

def test_hw():
    assert max_in_list([1,4,10,8]) == 10, "Should be 10"
    assert max_in_list([1, 4, 10, 12]) == 12, "Should be 12"
    assert max_in_list([-10, 100, 7]) == 100, "Should be 100"
    assert max_in_list([10, 5, 400, -9]) == 400, "Should be 400"
