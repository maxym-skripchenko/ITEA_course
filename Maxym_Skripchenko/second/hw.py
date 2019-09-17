# creating car and price variables
car = {"brand": "", "model": "", "color": "", "year": "", "engine_volume": "", "odometer": "", "phone_number": ""}
price = 0

# user input and price increase
car["brand"] = input("Input the brand of your car: ")
price += 10
car["model"] = input("Input the model of your car: ")
price += 10
car["color"] = input("Input the color your car was made: ")
price += 10
car["year"] = input("Input the year your car was created: ")
price += 10
car["engine_volume"] = input("Input the engine volume of your car: ")
price += 10
car["odometer"] = input("Input the odometer indicator of your car: ")
price += 10
car["phone_number"] = input("Input your phone number: ")
price += 10

# changing the variables type
car["year"] = int(car["year"])
car["odometer"] = int(car["odometer"])

# price change and output
price = (price * 10)/100
print("The price of your car is ", price)

# decreasing values of odometers and year
a = input("For how many years do you want to decrease your odometer? ")
b = input("For how many years do you want to decrease your year? ")
a = int(a)
b = int(b)
car["odometer"] -= a
car["year"] -= b

# outputting created cara
print(f"Your car brand is {car['brand']}, your car model is {car['model']}, the color of your car is {car['color']}, your car was made in {car['year']}, it's engine volume is {car['engine_volume']}, the odometer indicator is set on {car['odometer']}, and your phone number is {car['phone_number']}")