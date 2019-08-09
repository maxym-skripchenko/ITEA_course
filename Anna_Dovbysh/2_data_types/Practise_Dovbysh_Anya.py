import _string
import string
print('Hello! Enter information about yourself :')
#ввод информации от пользователя
name_input = input('First Name : ')
fam_input = input('Last Name : ')
mail_input = input('Email : ')
mail_input = str(mail_input)
age_input = input('Age : ')
age_input = int(age_input)
ph_num_input = input('Phone number : ')
ph_num_input = str(ph_num_input)

#проверяем имена
if name_input in string.ascii_letters and fam_input in string.ascii_letters:
    name_input is True and fam_input is True
    print(f'Your name: {name_input}, {fam_input}')
else: print('No name')

#проверяем номера телефонов
if '067' in ph_num_input or '097' in ph_num_input:
    operator = 'Kyivstar'
elif '095' in ph_num_input or '099' in ph_num_input:
    operator = 'Vodafone'
elif '063' in ph_num_input:
    operator = 'Lifecell'
else:
    operator = 'Not determined'
print(f'Your phone number belongs to {operator}')

#меняем тип данных для возраста и вызываем ошибку
try :
  age_input = str(age_input)
except ValueError as error:
    print('somthing broken: \n', error)
    age_input = 0
else: print(f'Your age : {age_input}')

'''#проверяем совершенолетие
if age_input<18:
    majority = 'minor'
else: age_input>=18
majority = 'adult'
print(f'You {majority}')
'''
#проверяем эл.почту
if 'gmail.com' in mail_input:
    mail = 'Google'
elif 'icloud.com' in mail_input:
    mail = 'Apple'
elif 'yandex.ru' in mail_input:
    mail = 'Yandex'
else:
    mail = 'Not determined'

print(f'Your email provider is {mail}')
