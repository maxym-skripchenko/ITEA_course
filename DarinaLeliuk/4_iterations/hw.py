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
