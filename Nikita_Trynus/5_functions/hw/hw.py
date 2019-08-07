def max_in_list(a_lot_of_numbers):

    max = 0
    for i in a_lot_of_numbers:

        if max < i : max = i

    return max

print(max_in_list([1,2,3,4,5,6,7]))