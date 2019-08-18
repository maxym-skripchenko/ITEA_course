from practise.pr1 import my_max
from practise.pr2 import my_length
from practise.pr3 import my_vowel
from practise.pr4 import my_sum, my_multiply
from practise.pr5 import my_is_member
from practise.pr6 import my_overlapping
from hw.hw1 import my_max_number

def test_my_max():
    assert my_max(7,78) ==78, "Should be 78"
def test_my_length():
    assert my_length("sfljn&&&999") == 11, "Should be 11"
def test_my_vowel():
    assert my_vowel("w") == False, "Should be False"
def test_my_sum():
    assert my_sum([1, 2, 3, 4, 7, 9, 89, 5634, 765]) == 6514, "Should be 6514"
def test_my_multiply():
    assert my_multiply([1, 2, 3, 4, 7, 9, 89, 5634, 765]) == 579989425680, "Should be 579989425680"
def test_my_is_member():
    assert my_is_member(["j", "e", "a", "hg"], "aw") == False, "Should be False"
def test_my_overlapping():
    assert my_overlapping(["j", "e", "a", "hg"], "aw") == True, "Should be True"
def test_my_max_number():
    assert my_max_number([3, 5, 7, 34, 6, -2, 42]) == 42, "Should be 42"
