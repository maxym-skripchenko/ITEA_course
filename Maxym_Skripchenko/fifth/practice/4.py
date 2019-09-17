def suma(a):
    count = 0
    for i in a:
        count += i
    return count


def mult(a):
    count = 1
    for i in a:
        count *= i
    return count


lists = [1, 2, 3, 4]

print(suma(lists))
print(mult(lists))