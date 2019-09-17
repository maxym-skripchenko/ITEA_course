def max_of_list(a):
    maximum = a[0]
    for count,i in enumerate(a,0):
        if i > maximum:
            maximum = a[count]
            if count == len(a) - 1:
                return maximum
        elif count == len(a) - 1:
            return maximum
        else:
            continue

lists = [11,4, 7, 30, 5, 50]
print(max_of_list(lists))