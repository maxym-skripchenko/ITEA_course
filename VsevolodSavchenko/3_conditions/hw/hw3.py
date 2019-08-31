##### start
###переменные
raiting = 50
favorite = ["GolfR32", "black"]
###ввод данных от пользователя + шаговое уменьшение
user_input_brand = input("Please select a car brand :")
raiting += 1
user_input_model = input("Please select a model :")
raiting += 1
user_input_color = input("Please select a color :")
raiting += 1
user_input_year = input("Please select the year of manufacture of the car :")
raiting += 1
user_input_engvol = input("Please choose engine volume:")
raiting += 1
user_input_odometer = input("Please select odometer :")
raiting += 1
user_input_phone = (input("Please Enter your phone number :"))
raiting += 1
###
if user_input_model in favorite and user_input_model in favorite:
    print("Nice choise!")
else:
    print(f"you select {user_input_model}, {user_input_color}", f"But {favorite} is better:)")
###
a = 1
try:
    b = user_input_year + a
    print(b)
except TypeError as error:
    user_input_year = int(input("enter year by number :"))
    a = 1
    print(user_input_year + a)
###
b = 0.1
try:
    print(user_input_engvol + b)
except TypeError as error:
    print (float(user_input_engvol) + b)
###
c = int(user_input_odometer)
if c < 1000:
    raiting += 2
elif 5000 < c < 100000:
    raiting += 1
else:
    c >= 100000
    raiting -= 1
###
print(f"Raiting of car: {raiting}")
#################2nd part
num = input("Write your card number :")
cvv = input("Your CVV :")
exp = input("expiration date (in format mm/yy)")
###
#d = len(num)
print(len(num))
if len(num) == 16:
    num = True
else:
    exit(1)
###
try:
    num1 = int(num)
except ValueError as error:
    print("Ups")
else:
    exit(1)
###
cvv = input("Your CVV :")
e = len(cvv)
if e < 3:
    exit(1)
else:
    print("Everything fine")
#####end