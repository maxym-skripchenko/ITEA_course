#. Write a Python program that accepts a string and calculate the number of digits and letters.

countdigits=0
countletters=0
while True:
    myinput = input("print your string")
    for elemet in myinput:
        if element.isdigit():
            countdigits +=1
        elif element.isalpha():
            countletters +=1
print(f'Number of letters: {countletters}, number of digits: {countdigits}')


#Write a Python program which iterates the integers from 1 to 50.
#For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".

series=range(1, 1, 50)
for element in series:
    if element % 15 == 0:
        print(f'FizzBuzz - {element}')
    elif element % 5 ==0:
        print(f'Buzz - {element}')
    elif element % 3 ==0:
        print(f'Fizz - {element}')