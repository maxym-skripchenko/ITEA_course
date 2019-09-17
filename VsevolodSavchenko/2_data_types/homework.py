#######################################
##########classwork
# add type Numbers_int
my_num_int = 11
print(my_num_int)
print(type (my_num_int))
# add type Numbers_float
my_num_float = 111.1
print(my_num_float)
print(type(my_num_float))
"""
add type Numbers_complex
my_num_complex = 111.1az
print(my_num_complex)
print(type(my_num_complex))
"""
# add type string
my_string = "let's try"
print(my_string)
print(type(my_string))
# add type list
my_list = [my_num_float, 222, "my_string", my_string]
print(my_list)
print(type(my_list))
# add type tuple
my_tuple = (True, 111, "my_string", my_string)
print(my_tuple)
print(type(my_tuple))
# add type dictionary
my_dict = {"lesson1": ["example1", "example2"], "lesson2": ["example3", "example4"] }
print(my_dict)
print(type(my_dict))
# add type set
my_set = set()
my_set.add(1)
my_set.add(2)
print (my_set)
print(type(my_set))
# add type bool
my_bool = 11
print(my_bool <= 1)
print (my_bool >= 1)
print (type (my_bool <= 1))
# use input
user_input_name = input("Enter your first name:")
user_input_surname = input("Enter your last name:")
user_input_phone = input("Enter your phone number:")
user_input_group = input("Enter your group:")
user_input_wishes = input("Enter your wishes for improvement:")
# use output + arithmetic operator
print ("student", user_input_name+user_input_surname, "phone number", user_input_phone, "group", user_input_group, "wish", user_input_wishes)
# use assignment operators
a = 10
b = 2
a //= b
print (a)

# use string formatting
print ("%.3s" % "let's try!")

#######################################
##########homework
first_price = 1000
# get information about brand
user_input_brand = input("Please select a car brand :")
first_price += 10
user_input_model = input("Please select a model :")
first_price += 10
user_input_color = input("Please select a color :")
first_price += 10
user_input_year = input("Please select the year of manufacture of the car :")
first_price += 10
user_input_engvol = input("Please choose engine volume:")
first_price += 10
user_input_odometer = input("Please select odometer :")
first_price += 10
user_input_phone = (input("Please Enter your phone number :"))
first_price += 10
print(first_price) # information about price
result = ((first_price*10)/100) #math result
print(int(result))
# finish car result
print("Your car is:", user_input_color, user_input_brand, user_input_model, user_input_year, user_input_engvol, user_input_odometer)


