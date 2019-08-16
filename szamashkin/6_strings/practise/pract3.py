def my_overlapping(string1, string2):
    for i in string1:
        for e in string2:
            if i == e:
                return True
    return False
print(my_overlapping([2, 5, 3], [4, 7, 5]))