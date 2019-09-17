from HW_7_Dovbysh_3 import first_in_list
from HW_7_Dovbysh_3 import last_in_list
from HW_7_Dovbysh_3 import rev_list
from HW_7_Dovbysh_3 import find_middle

def test_HW_7_3_firs_in_list():
    assert first_in_list(list(range(11))) == [0, 1, 2], 'Should be - [0, 1, 2]'

def test_HW_7_3_last_in_list():
    assert last_in_list(list(range(11))) == [8, 9, 10], 'Should be - [8, 9, 10]'

def test_HW_7_3_rev_list():
    assert rev_list(list(range(11))) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 'Should be - [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]'

def test_HW_7_3_find_middle():
    assert find_middle(list(range(11))) == 5, 'Should be - 5'

