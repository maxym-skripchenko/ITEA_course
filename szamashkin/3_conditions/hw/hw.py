#####Create rating value for car and increase or decrease at each step
rating = 10
brand = input("Your car brand is: ")
rating += 1
# added car brand name
model = input("Your car model is: ")
rating += 1
# added car model
color = input("Your car color is: ")
rating += 1
# added car color
year = input("Your car year_of_production is: ")
rating += 1
# added year_of_production
engine_volume = input("Your car engine_volume is: ")
rating += 1
# added engine_volume
odometer = input("Your car odometer info is: ")
rating += 1
# added odometer info
phone_number = input("Your phone_number is: ")
rating += 1
# added user phone number

#####Check that brand (model, color) not in your favourite, print brand name, and in finally clause print your favourite
price = 12000
print(price)
a = "Audi"; b = "Black"
if a in brand and b in color:
    print("You have a great car")
if a not in brand and b not in color:
    print("My favourite car is:" + str(b + a))
rating += 1
#print("My favourite is: Black Audi")

#####Try to change year type to int and catch exception, else print year and finally decrease year by 1 and print
try:
    print(int(year) - int("1"))
except ValueError:
    print("Error-year " + str(year) + " do not exist")

engine_volume = input("Your car engine_volume is: ")
rating += 1

#####Change Engine volume type to float and add 0.1 to value (print to user), (use try, except, else)
try:
    print(float(engine_volume))
except ValueError:
    print("Incorrect")
else:
    print(float(engine_volume) + float(0.1))
print("End of program")
rating += 1

"""Change odometer type to int check that odometer value less than 1000,greater than 50000, greater or equal to 100000 and  
set different value for rating"""

"""odometer = input("Your car odometer info is: ")
i = 1000; o = 50000; p = 100000
try:
    print(int(odometer))
except ValueError:
    print("Incorrect")
if i >= int(odometer):
    print("Rating of your car is 1")
if o >= int(odometer) or int(odometer) < o:
    print("Rating of your car is 2")
if p >= int(odometer) or int(odometer) < p:
    print("Rating of your car is 3")
if p <= int(odometer):
    print("Rating of your car is 4")
else:
    print("End of program")"""

x = int(input("Your car odometer info is: "))
if x <= 1000:
    rating += 1
if x >= 1000 or x <= 50000:
    rating += 1
if x >= 50000 or x <= 100000:
    rating -= 1
else:
    print("We will not buy your car")

rating += 1

#####Get final rating for your car by your criterion (3-4 if cases)
print(rating)