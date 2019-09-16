Shepard = {
    'type': 'dog',
    'owner name': 'Max',
    'eats': 'meat'}
Keks = {
    'type': 'cat',
    'owner name': 'Sergei',
    'eats': 'fish'}
Kris = {
    'type': 'Guinea Pig',
    'owner name': 'Kate',
    'eats': 'vegetables'}

pets = [Shepard, Keks, Kris]

for pet in pets:
    for key, value in pet.items():
        print(f'{key} : {value}')
