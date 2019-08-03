input('Hello, enter info :')

'''пользователь вводит данные по очереди'''

brand = input('Brand : ')
model = input('Model : ')
col = input('Color : ')
year = input('Year : ')
year = int(year)
'''присваиваем значение, введенное пользователем'''
year -= 2
'''уменьшаем получ. знач. на 2'''
eng_v = input('Engine volume : ')
odom = input('Odometer : ')
odom = int(odom)
'''присваиваем значение, введенное пользователем'''
odom -= 50
'''уменьшаем получ. знач. на 50'''
ph_num = input('Phone number : ')
user_input = input('input price car = ')
user_input = int(user_input)
'''присваеваем занчение, введенное пользователем'''
user_input += 10
'''увеличиваем получ. знач. на 10'''
new_price = (user_input * 10)/100
'''подсчитываем новое значение'''

'''выводим данные пользователю, с учетом измений значений'''

print(f'Your car brand is : { brand }')
print(f'Model : {model}')
print(f'Color : {col}')
print(f'Year : {year}')
print(f'Engine volume : {eng_v}')
print(f'Odometer : {odom}')
print(f'Phone number : {ph_num}')
print('new price car = ', new_price)
