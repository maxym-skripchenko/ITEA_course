#Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

series=range(1, 1, 50)
for element in series:
    if element % 5 == 0 and element % 3 == 0:
        print(f'FizzBuzz - {element}')
    elif element % 5 == 0:
        print(f'Buzz - {element}')
    elif element % 3 == 0:
        print(f'Fizz - {element}')