# creating variables and inputing users data
operators = ("Kuivstar", "Lifesell", "Vodafon")
provider = ("Google", "Apple", "Ukrnet")
first_name = input("Input your forst name: ")
last_name = input("Input your last name: ")
email = input("Input your email address: ")
age = input("Input your age: ")
phone_number = input("Input your phone number: ")

# if case for phone number
if "097" or "067" or "068" or "096" or "098" in phone_number:
    print(f"Your operator is {operators[0]}")
elif "063" or "073" or "093" in phone_number:
    print(f"Your operator is {operators[1]}")
elif "050" or "066" or "095" or "099" in phone_number:
    print(f"Your operator is {operators[2]}")
else:
    print("Invalid phone number, please, try again")
    exit(0)

# value error
try:
    age = int(age)
except ValueError:
    print("Age should be written by numbers like 1,2,3, ect")
else:
    print("Everything is fine")

# value creation in if cases
if age < 18:
    majority = "minor"
else:
    majority = "adult"

# email check
if "gmail.com" in email:
    print(f"{first_name} {last_name}, your internet provider is {provider[0]}")
elif "icloud.com" in email:
    print(f"{first_name} {last_name}, your internet provider is {provider[1]}")
elif "ukr.net" in email:
    print(f"{first_name} {last_name}, your internet provider is {provider[2]}")
else:
    print("Invalid input, please, try again")
    exit(0)

print(f"Hello, {first_name} {last_name}, a/an {majority} of {age} years old. Your phone number is {phone_number}, and your email address is {email}")