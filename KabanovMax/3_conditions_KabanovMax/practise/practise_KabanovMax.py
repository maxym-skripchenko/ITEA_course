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
phone_codes = {
	"kievstar": ("067", "096", "097", "098", "068"),
	"vodafone": ("050", "066", "095", "099"),
	"lifecell": ("063", "093", "073")
}

# Reciving output for mobile operator

if user_phone_number[:3] in phone_codes["kievstar"]:
	print("Your mobile operator is Kievstar")

elif user_phone_number[:3] in phone_codes["vodafone"]:
	print("Your mobile operator is Vodafone\MTS")

elif user_phone_number[:3] in phone_codes["lifecell"]:
	print("Your mobile operator is Life")

# Done with second task

# Third task

# Age become int, if not - error exception
try:
    user_age_int = int(user_age)
except ValueError as error:
	print("Invalid age")
while True:
	try:
		user_age = int(input("Age by number: "))
	except ValueError as error:
		print("Invalid age")
		continue
	else:
		user_age_int = int(user_age)
		print(user_age_int)
		break
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

if email_1 in user_email:
	print(f"You are using icloud")
elif email_2 in user_email:
	print(f"You are using gmail")
elif email_3 in user_email:
	print(f"You are using yandex")

# Done with sixth task

# Thank you for checking my practise, have a nice day)