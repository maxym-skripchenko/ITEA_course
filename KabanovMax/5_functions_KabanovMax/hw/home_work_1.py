def my_max_number(list):
    result = 0
    for number in list:
        if number > result:
            result = number
    return result

print(my_max_number([-3, 5, 12, 34, 159, -39, 1]))