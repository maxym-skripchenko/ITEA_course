'''Create car:

    * Use input for get:
        * Brand
        * Model
        * Color
        * Year
        * Engine volume
        * Odometer
        * Phone number'''


my_favorite_car = ["Audi", "A8", "White"]

# Create rating value for car and increase or decrease at each step

car_score = 0

user_input_car_brand = input("Please type car brand: ")

'''Check that brand (model, color) not in your favourite, print brand name, 
    and in finally clause print your favourite.'''

try:
    if user_input_car_brand not in my_favorite_car:
        print(f"You have selected {user_input_car_brand}")
finally:
    print(f"(By the way - my favorite car is {my_favorite_car[0]}:)")

car_score += 15

user_input_car_model = input("Please type car model: ")

car_score += 5

user_inuser_input_car_color = input("Please type car color: ")
car_score += 3.5

'''Try to change year type to int and catch exception, else print year  
and finally decrease year by 1 and print'''

while True:
    user_inpur_car_year = input("Please type year of manufacture: ")
    try:
        user_inpur_car_year = int(user_inpur_car_year)
    except ValueError:
        print("This field accepts digits only")
    else:
       user_inpur_car_year -= 1
       break
    finally:
        print(f"Let it be {user_inpur_car_year};)")


if user_inpur_car_year > 2010:
    car_score += 10
elif 1995 < user_inpur_car_year <= 2010:
    pass
else: car_score +- 10

'''Change Engine volume type to float and add 0.1 to value 
    (print to user), (use try, except, else)'''

while True:
    user_input_engine_volume = input("Please type engine volume: ")
    try:
        user_input_engine_volume = float(user_input_engine_volume)
    except ValueError:
        print("This field accepts digits only")
    else:
       break

user_input_engine_volume += 0.1
print(f"A technical details: let's decide volume is {user_input_engine_volume}")


if user_input_engine_volume > 3:
    car_score += 7
elif 1.5 < user_input_engine_volume <= 3:
    pass
else: car_score -= 2

'''Change odometer type to int check that odometer value less than 1000, 
    greater than 50000, greater or equal to 100000 and 
    set different value for rating'''

while True:
    user_input_odometer_value = input("Please type odometer value: ")
    try:
        user_input_odometer_value = int(user_input_odometer_value)
    except ValueError:
        print("This field accepts digits only")
    else:
       break

if user_input_odometer_value < 1000:
    car_score += 13
elif user_input_odometer_value > 50000:
    car_score -= 4.5
elif user_input_odometer_value >= 100000:
    car_score -= 8.5
else:
    pass

user_input_phone_number = input("Your phone number: ")
car_score += 1

# Get final rating for your car by your criterion

print(f"Your selection scores {car_score} points")