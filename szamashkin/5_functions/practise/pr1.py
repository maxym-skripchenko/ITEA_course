def my_max(a, b):
    if a > b:
        print("The biggest name is ", a)
        return a
    elif b > a:
        print("The biggest name is ", b)
        return b
    else:
        print("The numbers are the same")
        return
my_max(6,7)
my_max(7,78)