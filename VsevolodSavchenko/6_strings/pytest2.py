from hw.hw1 import map_to_lengths_for as my_map_to_lengths_for
from hw.hw2 import find_longest_word as longest
from practise.ex2 import is_palindrome as my_palindrome

def test_hw1_my_map_to_lengths_for():
    assert my_map_to_lengths_for("Hello") == 5, 'Should be 5'

def test_hw2_longest():
    assert longest(["qazwsxedc", "Hello, World", "TEST"]) == 12, 'Should be 12'

def test_ex2_my_palindrome():
    assert my_palindrome("radar") == True, 'Should be True'