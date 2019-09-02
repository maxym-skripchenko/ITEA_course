def my_overlapping(string_1, string_2):
    for list_1 in string_1:
        for list_2 in string_2:
            if list_1 == list_2:
                return True
    return False

print(my_overlapping([1, 2, 3], [4, 5, 6]))