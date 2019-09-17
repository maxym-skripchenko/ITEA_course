from Practise_6_Dovbysh_1 import generate_n_chars
from Practise_6_Dovbysh_2 import is_palindrome
from Practise_6_Dovbysh_3 import overlapping
from HW_6_Dovbysh_2 import find_longest_word
from HW_6_Dovbysh_3 import filter_long_word
from HW_6_Dovbysh_5 import valid_phone_number

def test_practise_6_1_generate_n_charm():
    assert generate_n_chars('x',5) == 'xxxxx', 'Should be - xxxxxx'

def test_practise_6_2_is_palindrome():
    assert is_palindrome('radar') == 'True', 'Shoud be True'

def test_practise_6_3_overlapping():
    assert overlapping(['ua'],['awed']) == 'True', 'Shoud be True'

def test_HW_6_2_find_longest_word():
    assert find_longest_word('AV is largest Analytics community of India') == 9, 'Shoud be 9'

def test_HW_6_3_filter_long_word():
    assert filter_long_word(['asad','ggfd','ff'],3) == ['asad', 'ggfd'], 'Shoud be - asad, ggfd'

def test_HW_6_5_valid_phone_number():
    assert valid_phone_number('+380977134900') == 'valid', 'Shoud be valid'