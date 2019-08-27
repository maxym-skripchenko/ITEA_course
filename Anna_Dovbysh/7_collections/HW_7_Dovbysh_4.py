names = {'name': ['Taras', 'Ivan', 'Inna', 'Roman', 'Alisa']}
numbers = {'number': [11, 7, 9, 19, 10]}

favorite_num = dict(names, **numbers)
print(favorite_num)

for key, value in favorite_num.items():
   print(key, ':', value)
