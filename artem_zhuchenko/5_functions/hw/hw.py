'''1. The function `max()` and `max_of_three()` from previous exercises
will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers,
or suppose we cannot tell in advance how many they are?
Write a function max_in_list()
that takes a list of numbers and returns the largest one.'''

my_list = list([- 5, 1, 3, 14, 2, -1, 10, 99, 0])
print(my_list)

def my_max_list(given_list):
    my_max = 0
    for element in given_list:
        if element > my_max:
            my_max = element
    return my_max


print(my_max_list(my_list))










