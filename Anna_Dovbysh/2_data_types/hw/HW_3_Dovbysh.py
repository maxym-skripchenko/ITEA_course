print('Enter info your credit card :')

#ввод информации от пользователя
numb_card = input('Credit card number : ')
cvv = input('cvv : ')
m_y = input('mm/yy: ')

#проверка количество цифр номера карты =16
assert len(numb_card) == 16

#изменение типа, ошибка и вывод
try:
  int(numb_card)
except ValueError as e:
    print(f'error : {e}')
else:

#проверка меньше 3
    if len(cvv) < 3:
        print('error cvv')
    else:

        print('Good')




'''ear = input('Year : ')
eng_vol = input('Engine volume :')
odom = input('Odometer : ')
odom = int(odom)
ph_num = input('Phone number : ')
#добавляем рейтинг
if  'bmw' or 'audi' or 'mercedes' in brand: rating_br = 3
elif 'toyota' or 'volksvagen' in brand: rating_br = 2
elif 'siat' or 'deo' in brand: rating_br = 1
else: print(f'not found brand')
if 'black' or 'white' in color: rating_c = 3
elif 'red' or 'green' in color: rating_c = 2
elif 'grey' in color: rating_c = 1
else: print(f'not found color')
if odom < 1000 : rating_o = 3
elif odom > 50000 and odom < 100000 : rating_o = 2
elif odom >= 100000 : rating_o = 1
else: print(f'not found')
#проверка любимой марки и цвета
fav_br = 'bmw'
fav_mod = 'x6'
fav_col = 'black'
if brand is not fav_br and model is not fav_mod and color is not fav_col:
    print('this brand not in my favourite')
else: print(f'My favourite car : {fav_br}, {fav_mod}, {fav_col}')
#изменение типа года, ошибка и вывод года, меншего на 1
try:
  int(year)
except ValueError: print('error')
else: print(f'Year : {year}')
finally: res = int(year) - 1
print(f'Correct year :{res}')
#изменение типа и вывод +0,1 к значению
try:
    float(eng_vol)
except ValueError: print('error')
else: eng_vol_new = int(eng_vol) + 0.1
print(f'Correct engineer volume: {eng_vol_new}')
#подсчет рейтинга и вывод
rating = rating_br + rating_c + rating_o
print(f'Your car rating: {rating}')
'''