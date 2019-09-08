##### start

KS1 = "+38067" ; KS2 = "+38098"; KS3 = "+38097"
lf1 = "063"; lf2 = "073"; lf3 = "093"
mts1 = "050"; mts2 = "066"; mts3 = "095"
age_majority = "18"
mail1 = "gmail.com" ; mail2 = "icloud.com"
###1 task
name = input("Please enter your first name :")
surname = input("Please enter your last name :")
email = input("Please enter your email :")
age = input("How old are you :")
phone = (input("Please enter your phone number +380 :"))
###2nd task
if KS1 in phone:
    print("Your phone number belongs to Kyivstar")
if KS2 in phone:
    print("Your phone number belongs to Kyivstar")
if KS3 in phone:
    print("Your phone number belongs to Kyivstar")
try:
    if lf1 in phone:
        print("Your phone number belongs to Life")
    if lf2 in phone:
        print("Your phone number belongs to Life")
    if lf3 in phone:
        print("Your phone number belongs to Life")
finally:
    if mts1 in phone:
        print("Your phone number belongs to MTS")
    if mts2 in phone:
        print("Your phone number belongs to MTS")
    if mts3 in phone:
        print("Your phone number belongs to MTS")
###3rd task
try:
    age = int(age)
except ValueError as err:
    print(err)
###5th task
if age < age_majority:
    print("minor")
else:
    if age >= age_majority:
        print("adult")
###6th task
if mail1 in email or mail2 in email:
    print(f"Your email provider is {email}")
else:
    print("Unknown email provider")