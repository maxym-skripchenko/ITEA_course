#######practise########
first_name = input("first name is: ")
last_name = input("last name is: ")
email = input("email is: ")
email_1 = "gmail.com"; email_2 = "icloud.com"
if email_1 in email:
    print("Your email provider is Google. It's cool!")
if email_2 in email:
    print("Your email provider is Apple. It's cool!")
else:
    print("You can go to hell")
def enterage(age):
    if age <= 0:
        raise ValueError("you have not yet been born")
    if age >= 100:
        print("you are very old")
    if age > 0 or age < 18:
        print("you are a minor")
    else:
        print("age is none, you are adult")
try:
    num = int(input("Enter your age: "))
    enterage(num)
except ValueError:
    print("you have not yet been born")
a = "067"; b = "098"; c = "097"
phone_number = input("your phone_number: ")
if a in phone_number:
    print("Your phone number belongs to Kyivstar")
if b in phone_number:
    print("Your phone number belongs to Kyivstar")
if c in phone_number:
    print("Your phone number belongs to Kyivstar")
else:
    if a or b or c not in phone_number:
         print("You are not in our team")
print(first_name, last_name, email, enterage, phone_number)
