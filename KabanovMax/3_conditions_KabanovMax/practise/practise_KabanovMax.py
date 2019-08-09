# 3_conditions practise from Kabanov Max

# First Task
# Reciving input from user
user_first_name = input("First Name: ")
user_last_name = input("Last Name: ")
user_email = input("Email: ")
user_age = input("Age: ")
user_phone_number = input("Phone Number without +38: ")


# Output for user
print(f'You are {user_first_name} {user_last_name}')
print(f'Your Email is {user_email}')
print(f'Your Age {user_age}')
print(f'Your Phone Number {user_phone_number}')
# Done with first task

# Second task
# Setting numbers for mobile operators
kievstar_1 = "067"
kievstar_2 = "096"
kievstar_3 = "097"
kievstar_4 = "098"
kievstar_5 = "068"

vodafone_1 = "050"
vodafone_2 = "066"
vodafone_3 = "095"
vodafone_4 = "099"

lifecell_1 = "063"
lifecell_2 = "093"
lifecell_3 = "073"

# Reciving output for mobile operator

if kievstar_1 in user_phone_number or kievstar_2 in user_phone_number or kievstar_3 in user_phone_number or kievstar_4 in user_phone_number or kievstar_5 in user_phone_number:
	print("Your mobile operator is Kievstar")

elif vodafone_1 in user_phone_number or vodafone_2 in user_phone_number or vodafone_3 in user_phone_number or vodafone_4 in user_phone_number:
	print("Your mobile operator is Vodafone\MTS")

elif lifecell_1 in user_phone_number or lifecell_2 in user_phone_number or lifecell_3 in user_phone_number:
	print("Your mobile operator is Life")

# Done with second task

# Third task

# Age become int, if not - error exception
try:
    print(int(user_age))
except ValueError:
    print("Invalid age")
# Done with third task

# Fifth task

# Setting age minority and majority
user_age_majority = "18"

if user_age < user_age_majority:
    print("You are too young")
else:
    if user_age >= user_age_majority:
        print("You are an adult)")

# Sixth task

# Setting emails

email_1 = "icloud.com"
email_2 = "gmail.com"
email_3 = "yandex.ru"

if email_1 in user_email or email_2 in user_email or email_3 in user_email:
	print(f"You are using this {user_email}")
else:
	print("You have unknown email=\ ")
# Done with sixth task

# Thank you for checking my practise, have a nice day)