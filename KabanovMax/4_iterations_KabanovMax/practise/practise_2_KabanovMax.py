'''
Practise #2
'''
# Setting input number for 4 odd and 6 even numbers

input_number = [1, 2, 3, 6, 9, 14, 19, 22, 37, 39]
odd = 0
even = 0

# Code for dividing input number for odd and even
for number in input_number:
    if number % 2:
        odd += 1
    else:
        even += 1
print(even, odd)

'''
End of practise #2
'''
