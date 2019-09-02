import re
import string




first_name = input('first name: ')
last_name = input('last name:')
email = input('email:')
age = input('age: ')
phone_number = input('phone number: ')

match = re.fullmatch('(?:097|067).*', phone_number)
if match:
    print('your phone number belongs to {}'.format('AT&T'))


try:
    age = int(age)

except ValueError:
    print(ValueError)
else:
    age = None
finally:
    age = int(input('age = '))

asc = string.ascii_letters
for i in first_name:
    if i in asc:
        continue
    else:
        print('NoName')

majority = 'adult' if age>18 else 'minor'
if re.fullmatch('.*gmail.com', email):
    print('google')
elif re.fullmatch('.*icloud.com', email):
    print('apple')