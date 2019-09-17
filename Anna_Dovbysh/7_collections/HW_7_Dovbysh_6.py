name_pet_1 = {'name': 'Tomas', 'type': 'cat', 'owner': 'Anya'}
name_pet_2 = {'name': 'Malysh', 'type': 'dog', 'owner': 'Sasha'}
name_pet_3 = {'name': 'Jeri', 'type': 'mouse', 'owner': 'Inna'}

pets = [name_pet_1, name_pet_2, name_pet_3]

for pet in pets:
    for key, value in pet.items():
        print(f'{key} : {value}')