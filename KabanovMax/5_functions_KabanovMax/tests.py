from hw.home_work_1 import my_max_number


def test_home_work_1():
    assert my_max_number([1, 2, 3, 4]) == 4, "Should be 4"
    assert my_max_number([1, 3, 6, 9]) == 9, "Should be 9"
    assert my_max_number([-10, 0, 10, 20]) == 20, "Should be 100"
    assert my_max_number([-100, -10, 0]) == 0, "Should be 0"


def test_practise_task_1():
    assert max_number(1, 4) == 4, "Should be 4"


def test_practise_task_2():
    assert my_length(hardwork) == 8, "Should be 8"


def test_practise_task_3():
    assert my_vowel("i") == True, "Should be True"


def test_practise_task_4():
    assert my_multiple([2, 2, 2]) == 8, "Should be 8"
    assert my_sum([2, 2, 2]) == 6, "Should be 6"


def test_practise_task_5():
    assert my_is_member(3, [1, 2, 3, 4]) == True, "Should be True"


def test_practise_task_6():
    assert my_overlapping([1, 2, 3], [3, 5, 6]) == True, "Should be True"


print("Everything passed")