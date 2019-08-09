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

#2#
for fizzbuzz in range(30):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
print("End of program")

#2.1#
list = []
for i in range(1, 30):
    if i % 3 == 0 and i % 5 == 0:
        list.append("FizzBuzz")
    elif i % 3 == 0:
        list.append("Fizz")
    elif i % 5 == 0:
        list.append("Buzz")
    else:
        list.append(i)
print(list)
print("End of program")