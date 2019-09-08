#Define a function `overlapping()` that takes two lists and
#returns True if they have at least one member in common,
#False otherwise. You may use your `is_member()` function,
#or the in operator, but for the sake of the exercise,
#you should (also) write it using two nested for-loops.

def overlapping(first_list, second_list):
    for element_from_first in first_list:
        for element_from_second in second_list:
            if element_from_first == element_from_second:
                return True
    return False

