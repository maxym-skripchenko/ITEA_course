
def max_in_list(a_lot_of_numbers):

    max = 0
    for i in a_lot_of_numbers:

        if max < i : max = i

    return max



def test_func():
    assert max_in_list([1,2,3])==3


def test_func1():
    assert max_in_list([100,2,1])==100


def test_func2():
    assert  max_in_list([])==0