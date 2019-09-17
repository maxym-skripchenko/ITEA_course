# foo = "foo"
# bar = "bar"
# baz = "bar"

'''
c = foo + bar + baz

print(c)

res = foo * 5

print(res)
'''
'''
res = foo * 5

foo_in_res = foo in res

print(foo_in_res)

vowels = ["s", "a", "b"]

for vowel in vowels:
	if vowel in res:
'''
'''
abc = "asdfg"
print(abc[1])
print(abc[-1])
print(abc[-2])

s = "foobar"

print(s[1:])
print(s[2:5])
# print(s[1:-1])
# print(s[:-3])
'''
#
# # s = "foobar"
# s = "0123456789"
# print(s[::2])
#
#
# # 1 с какого начинает
# # 2 заканчивает
# # 3 это шаг
# # пустые указывают весь размер
#
# print(s[0:6:2])
# print(s[1:9:3])
# print(s[::3])
# print(s[::-1])
#
#
# my_list = [1,2,3]
# my_list[2] = 5
# print(my_list)
#
# my_tuple = (1,2,3)
# my_tuple[2] = 5
# print(my_tuple)
# #  не работает тюпл так

# string = "abcde"
# # string[4] = "f" #будет с ошибкой нельзя так
# my_string = string[:-1] + "f"
# print(my_string)

# string = "my string"
# print(string.capitalize())
# # вывод первую букву большой
# print(string)
# string = string.capitalize()
# print(string)

# string = "my string"
# print(string.count("a"))
# считает сколько букв а в стринге

# string = "my string"
# print(string.find("r"))
# # находит букву и определяет ее цифрой. 5 для р
#
# string = "my string"
# print(string.index("a"))
# # находит букву и определяет ее цифрой. 5 для р

# print(".".join(["a","b","c"]))
# # точка соеденит все елементы в стринге


# string = "String"
# print(string.strip("ri"))
# # уберет указанный элемент. влево вправо могут убрать славе или справа указанный элемент


# string = "String"
# print(string.replace("i", "ooo"))
# # заменяет первый элемент на второй элемент

# string = "String String"
# print(string.split(" "))
# # переводит стринг в лист. join может соеденить назад в стринг

import re

# p = re.compile("[a-z]+") # только нижний
# #p = re.compile("[a-zA-Z]+") # весь алфавит нижний и верхний
# # p.match("abcd")
# m = p.match("emTpo")
# # патерн алфивати проверит М и скажет есть совпадение или нет в алфавите
#
# res = m.group()
# print(res)
# # выводит только ем что которые совпали с алфавитом в малом регистре



