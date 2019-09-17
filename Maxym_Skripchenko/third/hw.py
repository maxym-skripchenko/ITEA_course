# first task: car creation
# list of favourite colors and brands
fav_colors = {"Red", "Black", "Blue"}
fav_brand = {"Porsche", "Mitsubishi", "Ford"}

# car creation and user input
car = {"brand": "", "model": "", "color": "", "year": "", "engine_volume": "", "odometer": "", "phone_number": ""}
car["brand"] = input("Input the brand of your car: ")
car["model"] = input("Input the model of your car: ")
car["color"] = input("Input the color your car was made: ")
car["year"] = input("Input the year your car was created: ")
car["engine_volume"] = input("Input the engine volume of your car: ")
car["odometer"] = input("Input the odometer indicator of your car: ")
car["phone_number"] = input("Input your phone number: ")

# creating rank variable
rank = 5

# color and brand influence on rank
if car["color"] not in fav_colors:
    rank -= 1
else:
    rank += 1

if car["brand"] not in fav_brand:
    rank -= 1
else:
    rank += 1

# year value error
try:
    car["year"] = int(car["year"])
except ValueError:
    print("Please, input car year by numbers like 1,2,3, etc")
else:
    print(f'Inputed year is {car["year"]}')
finally:
    car["year"] -= 1

if car["year"] < 2000:
    rank -= 1

# engine volume setting
try:
    car["engine_volume"] = float(car["engine_volume"])
except ValueError:
    print("Engine volume must be a number!")
else:
    car["engine_volume"] += 0.1

if car["engine_volume"] < 1.1:
    rank -= 2
if 1.2 < car["engine_volume"] < 1.5:
    rank -= 1
if car["engine_volume"] > 3.5:
    rank += 1

# odometer if case
try:
    car["odometer"] = int(car["odometer"])
except ValueError:
    print("Odometer indicator must be a number")
else:
    if car["odometer"] < 1000:
        rank += 2
    if car["odometer"] > 50000:
        rank -= 1
    if car["odometer"] > 100000:
        rank -= 2

print(f"Your car brand is {car['brand']}, your car model is {car['model']}, the color of your car is {car['color']}, your car was made in {car['year']}, it's engine volume is {car['engine_volume']}, the odometer indicator is set on {car['odometer']}, and your phone number is {car['phone_number']}")
print(f"The rating of your car is {rank}")

# second task: credit card
# variables creation and inputs
card = {"number": "", "cvv": "", "year": ""}
card["number"] = input("Input your credit card number: ")
card["cvv"] = input("Input CVV code on the back of your card")
card["year"] = input("Input month and year of your card (mm/yy)")

if len(card["number"]) < 16:
    exit(0)

try:
    card["number"] = int(card["number"])
except ValueError:
    print("OK")

if len(card["cvv"]) < 3:
    print("Error")
    exit(0)

print("Everything fine")