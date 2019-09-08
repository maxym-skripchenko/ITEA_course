'''
Practise #1
'''
numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Creating list of numbers

# Making code for exception
numbers_2 = []
for element in numbers_list:
    if element == 3 or element == 6:
        continue
    elif element > 6:
        break
    #print(element)
    numbers_2.append(element)

# Results
print(numbers_2)

'''
End of practise #1
'''