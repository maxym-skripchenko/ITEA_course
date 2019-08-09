'''2. Write a Python program which iterates the integers from 1 to 50.
For multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".'''

boring_numbers = tuple(range(1, 51))               #Setting tuple with numbers range

print(boring_numbers)
for element in boring_numbers:
    if element % 3 == 0 and element % 5 != 0:      #Avoid printing "Fizz" to the numbers where it should be "FizzBuzz"!
        print("Fizz")
    if element % 5 == 0 and element % 3 != 0:      #Avoid printing "Buzz" to the numbers where it should be "FizzBuzz"!
        print("Buzz")
    if element % 3 == 0 and element % 5 == 0:
        print("FizzBuzz")
    if element % 5 != 0 and element % 3 != 0:
        print(element)