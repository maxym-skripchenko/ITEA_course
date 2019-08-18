'''1. Write a Python program that accepts a string
and calculate the number of digits and letters.
isdigit()
isalpha()'''

user_input_username = input("Please type username: ")                     #Accept string from user

user_input_username_character_list = list(user_input_username)            #Turn user input into list of characters

count_digits = 0                                                          #Create variables to count digits and letters
count_alpha = 0
count_other_characters_and_spaces = 0

for element in user_input_username_character_list:                        #Set loop to define type of character
    if element.isdigit() == True:
        count_digits += 1
    if element.isalpha() == True:
        count_alpha += 1
    else:
        count_other_characters_and_spaces += 1


print(f"Username contains {count_digits} digits!")                                                      #Print results
print(f"Username contains {count_alpha} letters!")
print(f"Username contains {count_other_characters_and_spaces} other characters and spaces!")



