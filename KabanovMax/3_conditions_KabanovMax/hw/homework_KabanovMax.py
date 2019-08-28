# 3_conditions Homework form Kabanov Max

"""
First task
First Step
"""
# First value of raiting
initial_rating = 90

# Code for receiving info from user

user_input_car_brand = input("Please insert car brand: ")
initial_rating += 10
# Receive car brand and adding

user_input_car_model = input("Which model: ")
initial_rating -= 10
# Receive car model and subtracting

user_input_car_color = input("What color do you prefer: ")
initial_rating -= 10
# Receive car color and subtracting

user_input_car_year_manufacturing = input("Desired year of manufacturing: ")
initial_rating += 10
# Receive car year and adding

user_input_car_engine_volume = input("Set engine volume: ")
initial_rating += 10
# Receive car engine volume and adding

user_input_car_odometer = input("Please select odometer: ")
initial_rating -= 10
# Receive car odometer and subtracting

user_input_phone_number = input("For callback enter your phone number: ")
initial_rating += 10
# Receive phone number and adding

'''
Second Step
'''
# Setting my favorites
my_favorites = ['Tesla', 'model 3', 'silver']

# Comparison of my favorites with user favorites
if user_input_car_brand in my_favorites and user_input_car_model in my_favorites and user_input_car_color in my_favorites:
	print("Nice choise!")
else:
	print(f"Your choise is {user_input_car_brand}, {user_input_car_model}, {user_input_car_color} not bad",
		  f"Would you like to try {my_favorites}?")

'''
Third Step
'''

# Setting value for age changing
year_value = 3

# Trying to catch error and subtracting year by 3
try:
	car_year_manufacturing = int(user_input_car_year_manufacturing) - year_value
	print(car_year_manufacturing)
except ValueError as error:
	while True:
		try:
			user_year_input = int(input("Please set year of manufacturing by number (2019 a. e.): "))
		except Exception as error:
			continue
		else:
			break
	print(user_year_input - year_value)

'''
Fourth step
'''

# Setting value for float changing
float_value = 0.1

# Trying to catch error and adding 0.1 to engine volume as float
try:
	car_new_float = float(user_input_car_engine_volume) + float_value
except ValueError as error:
	while True:
		try:
			user_input_car_engine_volume = (input("Please set engine volume by number (1.6 a. e.): "))
			car_new_float = float(user_input_car_engine_volume) + float_value
		except ValueError as error:
			continue
		else:
			car_new_float = float(user_input_car_engine_volume) + float(float_value)
			break

print(car_new_float)

'''
Fifth step
'''

# Changing odometer type to int
odometer_int = int(user_input_car_odometer)

if odometer_int < 1000:
	initial_rating += 30
elif 1000 < odometer_int < 5000:
	initial_rating += 10
else:
	odometer_int >= 5000
	initial_rating -= 20

'''
Sixth step
'''

print(f"Your car rating is: {initial_rating}")

'''
End of first task of HomeWork 
'''

'''
Homework with credit card
'''

# Code for receiving info from user credit card

input_credit_number = input("Type your card number: ")
input_credit_cvv = input("Type your CVV number: ")
input_credit_year = input("Type your expiration date in format mm\yy : ")

# Checking card length and exiting if False

credit_length = len(input_credit_number)

if len(input_credit_number) == 16:
	credit_length = True
else:
	exit(1)

# Setting card number to int. if error will be caught set to exit

try:
	credit_int = int(input_credit_number)
except ValueError as error:
	exit(1)
else:
	print("OK")

# Checking all info

if len(input_credit_number) != 16 and len(input_credit_cvv) != 3 and len(input_credit_year) != 5:
	exit(1)
else:
	print("Everything fine")

'''
End of Homework. Thx for checking, have a nice day=)
'''