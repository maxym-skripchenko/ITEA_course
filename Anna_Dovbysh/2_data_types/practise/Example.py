''' разные переменные '''
a = 12
b = 10
c = 3
name = 'Ann'
age = 26
day = 'monday'
fl_num = 3.14
fl_num2 = 4.18
my_bool = True
my_bool2 = False
my_list = [a, b, c]
num_home = (1, 2, 3, 4)
my_set = {1, 2, 2, 3, 6, 6}
info = {'viddil': ['IT', 'HR', 'BDO'], 'viddil2': ['BI', 'F&A']}

''' определение и вывод типа '''
print('type a -',type(a))
print('type b -',type(b))
print('type c -',type(c))

print('type name -', type(name))

print('type age - ', type(age))

print('type day - ', type(day))

print('type fl_num - ', type(fl_num))
print('type fl_num - ', type(fl_num2))

print('type my_bool -', type(my_bool))
print('type my_bool2 - ', type(my_bool2))

print('my_list = ', my_list)
print('type -', type(my_list))
print('my_list[2] = ', my_list[2])

print('type num_home -', type(num_home))
print(num_home)

print('my_set =', my_set)
print('type my_set - ', type(my_set))

print(info['viddil'])
print('type info - ', type(info))

'''ввод/вывод инфы'''
name_input = input('First Name : ')
fam_input = input('Last Name : ')
tel_input = input('Phone number : ')
gr_input = input('Group : ')
let_input = input('a, b, c, d : ')

print(input)

'''Arithmetic operators'''
d = a + b
fl_num3 = fl_num2 - fl_num
print('znach d = ', d)
print('znach fl_num3 = ', fl_num3)

'''Assignment operators'''
d += c
a /= d
print('znach a = ', a)

'''String formatting'''
print(f'Hello, {name}. You are {age} year.')

