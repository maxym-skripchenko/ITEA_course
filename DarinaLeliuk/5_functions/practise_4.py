#4. Define a function `sum()` and a function `multiply()` that
#sums and multiplies (respectively) all the numbers in a list
#of numbers. For example, `sum([1, 2, 3, 4])` should return 10,
#and `multiply([1, 2, 3, 4])` should return `24`.

def my_sum(some_list_of_numbers):
    my_result = 0
    for element in some_list_of_numbers:
        my_result += element
    return my_result

def my_multiple(some_list_of_numbers):
    my_multiplication = 1
    for element in some_list_of_numbers:
        my_multiplication = my_multiplication * element
    return my_multiplication




