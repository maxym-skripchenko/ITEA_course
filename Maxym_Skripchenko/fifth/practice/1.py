def maxi(a, b):
    if a > b:
        return print(a, "is bigger")
    else:
        return print(b, "is bigger")


a = int(input("Input a: "))
b = int(input("Input b: "))
print(maxi(a, b))