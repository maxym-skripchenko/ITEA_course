for element in range(50):
    if element % 3 == 0 and element % 5 == 0:
        print("fizzbuzz")
        continue
    elif element % 3 == 0:
        print("fizz")
        continue
    elif element % 5 == 0:
        print("buzz")
        continue
    print(element)