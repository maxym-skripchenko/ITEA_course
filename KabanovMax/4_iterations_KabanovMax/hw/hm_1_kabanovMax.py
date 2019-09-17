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
digit_numbers = len(number_of_digits)
letter_numbers = len(number_of_letters)

print(f"The number of digits: {digit_numbers}")
print(f"The number of letters: {letter_numbers}")

'''
End of Homework #1
'''