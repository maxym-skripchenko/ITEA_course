def my_overlapping(string1, string2):
    for element in string1:
        for element1 in string2:
            if element == element1:
                return True
    return False
print(my_overlapping([2, 5, 3], [4, 7, 5]))