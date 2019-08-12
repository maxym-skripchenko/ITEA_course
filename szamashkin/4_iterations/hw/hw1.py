#1#
a = input("Print something: ")
digits = letters = 0
for c in a:
    if c.isdigit():
        digits = digits + 1
    elif c.isalpha():
        letters = letters + 1
    else:
        pass
print("Letters", letters)
print("Digits", digits)
print("End of program")