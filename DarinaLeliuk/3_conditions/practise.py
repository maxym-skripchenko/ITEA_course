#Use input/output for get:* First Name* Last Name* Email* Age* Phone number

inputfn=input("Would you be so kind to tell your first name")
inputln=input("Would you be so kind to tell your last name?")
inputage=input("Would you be so kind to tell your age?")
inputphn=input("Would you be so kind to tell your phone number?")
inputem=input("Would you be so kind to tell your email?")

#2. If phone number starts from (097, 067) output "Your phone number belongs to {}" and create variable operator with value.

if int(inputphn[:3]) is "097" or "067":
    operator="Kyivstar"
    if int(inputphn[:3]) is "093":
        operator="Life"
    else:
        operator="other"
print(f"Your phone number belongs to {operator}")

#3. Try to change age from str to int and catch Exception (ValueError), set age None in else case

try:
    int(inputage)
except ValueError:
    print("Not valid value for age")
    age="None"
else:
    age=int(inputage)

#4. Check that First Name consist of letters (string.ascii_letters) else set "No name"

try:
    string.ascii_letters(inputfn)
except ValueError:
    print("Not valid value for first name")
    firstname="No name"
else:
    firstname=inputfn

#5. Create variable majority and set 'minor' if age less than 18, in other case set 'adult'

if int(inputage)<18:
    group="minor"
else:
    group="adult"

#6. If email ends with gmail.com, icloud.com…make output ”Your email provider is {}”Use output for print: First Name, Majority

if inputem[-9] is "gmail.com":
    em="Google"
else:
    if inputem[-10] is "icloud.com":
        em="Apple"
    else:
        em="some else"

print("Your email provider is {em}")

#7. Output result of each variable
print(f"Your name is {firstname} {inputln}, your age is {age}, your phone number is {inputphn}, it belongs to {operator} mobile operator. You belong to {group} user group")
