def overlapping(list1, list2):
    for value1 in list1:
        for value2 in list2:
            if value1 == value2:
                return True
    return False

print(overlapping([1, 11], [2, 22]))
print(overlapping([1, 11], [11, 22]))
print(overlapping(["a", "b", "c"], ["c", "d"]))
print(overlapping(["a", "b", "c"], ["d", "e"]))