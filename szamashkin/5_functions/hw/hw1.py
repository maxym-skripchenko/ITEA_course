def my_max_number(list):
    result = 0
    for x in list:
        if x > result:
            result = x
    return result
print(my_max_number([3, 5, 7, 34, 6, -2, 42]))