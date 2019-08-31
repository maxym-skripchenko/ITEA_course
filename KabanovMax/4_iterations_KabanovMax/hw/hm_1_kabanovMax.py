'''
Homework #1 KabanovMax
'''

# Input of string
input_text = str(input("Type your message here: "))

# Calculating digits
number_of_digits = [d for d in input_text if d.isdigit()]

# Calculating letters
number_of_letters = [l for l in input_text if l.isalpha()]

# Output string and quantity
print(f"The number of digits: {number_of_digits}")
print(len(number_of_digits))
print(f"The number of letters: {number_of_letters}")
print(len(number_of_letters))

'''
End of Homework #1
'''