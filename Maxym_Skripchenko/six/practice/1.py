def generate_n_chars(a, b):
    st = ""
    while a > 0:
        st += b
        a -= 1
    return st

a = int(input("How many?: "))
b = input("What letter?: ")
print("Your string is ", generate_n_chars(a,b))