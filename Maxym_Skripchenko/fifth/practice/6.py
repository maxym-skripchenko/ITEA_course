def my_len(a):
    count = 0
    for i in a:
        count += 1
    return count


def overlapping(a, b):
    for count, i in enumerate(a, 0):
        for counter, j in enumerate(b, 0):
            if type(i) != type(j):
                return False
            else:
                if i == j:
                    return True
                elif i != j and count == len_1 - 1 and counter == len_2 - 1:
                    return False
                else:
                    continue
        continue


a = [1, 2, 3, 8, 9, 0, 15]
len_1 = my_len(a)
b = [4, 6, 7, 15]
len_2 = my_len(b)
print(overlapping(a, b))