import re
my_list = 'anndov@gmail.com, sasha2@yandex.ru, semen09@mail.ru, misha3@ukr.net'
result = re.findall(r'@\w+.\w+', my_list)
print(result)