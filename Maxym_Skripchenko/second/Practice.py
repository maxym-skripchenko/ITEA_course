# creating your variables
integer = 1
booling = True
double = 2.0
message = "Hello"
tup = (integer, double, message)
sett = {integer, double, message}
lists = [integer, double, message]
dictionary = {"key": integer, "key2": double,    "key3": message}

# print your variables and their types
print("integer is ", integer, "and it's type is", type(integer))
print("booling is ", booling, "and it's type is ", type(booling))
print("double is ", double, "and it's type is", type(double))
print("message is ", message, "and it's type is", type(message))
print("tup is ", tup, "and it's type is", type(tup))
print("sett is ", sett, "and it's type is", type(sett))
print("lists is ", lists, "and it's type is", type(lists))
print("dictionary is ", dictionary, "and it's type is", type(dictionary))

# waiting for users input for different tasks
first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
phone_number = input("Input your phone number: ")
group = input("Enter your group: ")
a = input("a: ")
b = input("b: ")
c = input("c: ")
d = input("d: ")

# converting inputed a,b,c,d to float
a = float(a)
b = float(b)
c = float(c)
d = float(d)

# printing inputs of the user
print("Your first name is ", first_name)
print("Your last name is ", last_name)
print("Your phone number is ", phone_number)
print("Your group is ", group)

# arithmetical operations
print("a+b= ", int(a) + float(b))
print("a-b= ", int(a) - float(b))
print("a*b= ", int(a) * float(b))
print("a%b= ", int(a) % float(b))
print("a//b= ", int(a) // float(b))
print("a**b= ", int(a) ** float(b))

# assignment operators
a += float(b)
print(a)
b -= float(c)
print(b)
c *= float(d)
print(c)
d %= float(a)
print(d)
a //= float(b)
print(a)
b **= float(c)
print(b)

# string formation
print(f"Your first name is {first_name}, and your last name is {last_name}")
print("Your first name is %s, and your last name is %s" % (first_name, last_name))
