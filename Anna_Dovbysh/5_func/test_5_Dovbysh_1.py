from Practise_5_Dovbysh_1 import my_max
from Practise_5_Dovbysh_2 import length
from Practise_5_Dovbysh_3 import vowel_or_not
from Practise_5_Dovbysh_4 import my_sum
from Practise_5_Dovbysh_4 import my_multiply
from Practise_5_Dovbysh_5 import  my_is_member
from Practise_5_Dovbysh_6 import my_overlapping
from HW_5_Dovbysh import my_max_in_list

def test_practise_5_1_max():
    assert my_max([1,2]) == 2, 'Should be 2'

def test_practise_5_2_my_length():
    assert length([1,2,2]) == 3, 'Should be 3'

def test_practise_5_3_vovel():
    assert vowel_or_not('a') == True, 'Should be True'

def test_practise_5_4_my_sum():
    assert my_sum([1,2,3,4]) == 10, 'Should be 10'

def test_practise_5_4_my_multiply():
    assert my_multiply([1, 2, 3, 4]) == 24, 'Should be 24'

def test_practise_5_5_my_is_mem():
    assert my_is_member(2, [2,3,4]) == True, 'Should be True'

def test_practise_5_6_my_overlap():
    assert my_overlapping([1,2,4],[6,4,5]) == True, 'Should be True'

def test_HW_5_my_max_in_list():
    assert my_max_in_list([1,5,10,6]) == 10, 'Should be 10'
