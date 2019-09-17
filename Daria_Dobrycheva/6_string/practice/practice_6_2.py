import re

def is_palindrome(inputString):
    inputString = re.sub('[^a-zA-Z0-9]', '', inputString)
    reversedString = inputString[::-1]

    if inputString.lower() == reversedString.lower():
        return True
    else:
        return False


A = input('Enter the string to check palindrome: ')

if is_palindrome(A) == True:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
