from hw.HW import max_in_list as my_max_list
from practise.ex1 import max as my_max
from practise.ex2 import length as my_length
from practise.ex3 import is_vowel as my_is_vowel
from practise.ex4 import sum as my_sum, multiply as my_multiply
from practise.ex5 import is_member as my_is_member
from practise.ex6 import overlapping as my_overlapping

def test_homework_HW_my_max_list():
    assert my_max_list([1,3,5]) == 5, "Should be 5"

def test_practise_ex1_my_max():
    assert my_max(11,111) ==111, "Should be 111"

def test_practise_ex2_my_length():
    assert my_length("qazwsxedc") == 9, "Should be 9"

def test_practise_ex3_my_is_vowel():
    assert my_is_vowel("A") == True, "Should be True"
    assert my_is_vowel("b") == False, "Should be False"

def test_practise_ex4_my_sum():
    assert my_sum([1,2,3]) == 6, "Should be 6"
    assert my_multiply([2,4,3]) == 24, "Should be 24"

def test_practise_ex5_my_is_member():
    assert my_is_member("c", ["b", 1, "c"]) == True, "Should be Ttue"

def test_practise_ex6_my_overlapping():
    assert my_overlapping(["a", "b", "c"], ["d", "e"]) == False, "Should be False"