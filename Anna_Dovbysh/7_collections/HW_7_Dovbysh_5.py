my_glossary = {'boolean': 'boolean True or False',
               'float': 'floating point number',
               'int': 'integer',
               'str': 'strings',
               'complex': 'complex numbers'}

print(*my_glossary.items())

for key, value in my_glossary.items():
    print(f'{key} : {value}')

print(*my_glossary.items(), sep='\n')