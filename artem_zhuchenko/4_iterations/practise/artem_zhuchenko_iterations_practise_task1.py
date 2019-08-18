'''1. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5'''


my_tuple = (0, 1, 2,  3, 4, 5, 6)       #create tuple
for element in my_tuple:
    if element == 3 or element == 6:    #excluding 3 & 6
        continue
    elif element > 6:
        break                           #end iteration
    print(element)
