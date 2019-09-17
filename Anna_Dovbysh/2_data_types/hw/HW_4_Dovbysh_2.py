num = range(51)
for element in num:
     if element % 3 == 0 and element % 5 == 0:
        print(f'{element} FizzBuzz')
     elif element %3 == 0:
        print(f'{element} Fizz')
     elif element %5 == 0:
        print(f'{element} Buzz')
