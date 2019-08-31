#1. Define a function `max()` that takes two numbers as arguments
#and returns the largest of them. Use the if-then-else construct
#available in Python.

def my_max(first_number, second_number):
    if first_number>second_number:
        return first_number
    elif first_number<second_number:
        return second_number
    else:
        return ("They are equal")

result=my_max(2, 2)
print(result)



