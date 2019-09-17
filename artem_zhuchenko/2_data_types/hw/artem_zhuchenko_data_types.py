#creating car price

car = 100000

#warning the user of increase
print("Price start from 100000$. Please type your parameters. Each one costs 10$.")

#Get car brand:
desired_brand = input("Please type desired car brand: ")

car += 10

#Get car model
desired_model = input("Please type desired model: ")

car += 10

#Get color
desired_color = input("Please type desired color: ")

car += 10

#Get car year
desired_year = input("Please type year: ")

car += 10

#Get engine volume
desired_engine_volume = input("Please type desired engine volume: ")

car += 10

#Get odometer value
desired_odometer_value = input("Please type odometer value: ")

car += 10

#Get customer phone number
user_input_phone_number = input("Please enter your phone number: ")

car += 10

#to view price after specifying parameters
print(car)

#to calculate final price after applying some coefficients
total = ((car*10)/100)

#transform user input year from string into integer:
year = int(desired_year)

#decrease year
year -= 2

#transform user input engine volume from string into integer:
odometer = int(desired_odometer_value)

#decrease volume
odometer -= 20000

#showing car summary


print("Your selection is: ", desired_brand, desired_model, "of ", year, "in ",desired_color, "with ", desired_engine_volume, "L engine and of ", odometer, "miles experience")
print("Price: ", total)

#the end.
