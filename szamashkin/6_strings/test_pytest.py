from hw.hw1 import map_to_lengths_for
from hw.hw2 import find_longest_word
from hw.hw3 import filter_long_words
from practise.pract1 import generate_n_chars
from practise.pract2 import is_palindrome
from practise.pract3 import my_overlapping

def test_map_to_lengths_for():
    assert map_to_lengths_for(["qwerty"]) == [6], "Should be 6"
def test_find_longest_word():
    assert find_longest_word(["hello", "Ukraine"]) == "Ukraine", "Should be Ukraine"
def test_filter_long_words():
    assert filter_long_words(['this','is','a','word'],1) == ['this', 'is', 'word'], "Should be ['this', 'is', 'word']"
def test_generate_n_chars():
    assert generate_n_chars(2, "Key") == "KeyKey", "Should be KeyKey"
def test_is_palindrome():
    assert is_palindrome("pineapple") == False, "Should be False"
def test_my_overlapping():
    assert my_overlapping([2, 5, 3], [4, 7, 5]) == True, "Should be True"
