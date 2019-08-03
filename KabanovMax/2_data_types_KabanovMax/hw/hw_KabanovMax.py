initial_price = 35000
#First value

#Code for reciving info from user
user_input_car_brand = input("Please insert car brand: ")
initial_price += 10
#Receive car brand and adding
user_input_car_model = input("Which model: ")
initial_price += 10
#Receive car model and adding
user_input_car_color = input("What color do you prefer: ")
initial_price += 10
#Receive car color and adding
user_input_car_year_manufacturing = input("Desired year of manufacturing: ")
initial_price += 10
#Receive car year and adding
user_input_car_engine_volume = input("Set engine volume: ")
initial_price += 10
'''Have no idea hot to define Tesla engine volume =)
Receive car engine volume and adding
'''
user_input_car_odometer = input("Please select odometer: ")
initial_price += 10
#Receive car odometer and adding
user_input_phone_number = input("For callback enter your phone number: ")
initial_price += 10
#Receive phone number and adding

#print(initial_price)
#to show me value for price after gathering info about user

final_price = ((initial_price*10)/100)
#magic step of dividing

int_user_input_car_year_manufacturing = int(user_input_car_year_manufacturing)
int_user_input_car_year_manufacturing -= 5

int_user_input_car_engine_volume = int(user_input_car_engine_volume)
int_user_input_car_engine_volume -= 1
#Setting string object to integer by using Google and making Holy Decreasing


print("You choose this car: ",user_input_car_brand, user_input_car_model, user_input_car_color, int_user_input_car_year_manufacturing, int_user_input_car_engine_volume, user_input_car_odometer)
print("This car cost: ", final_price)
'''Final step in HW
Hope you enjoy my Home Work and have a nice day
'''