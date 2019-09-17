pets = []
pet = {
    "animal type": "dog",
    "name": "Barbos",
    "owner": "Misha",
    }
pets.append(pet)

pet = {
    "animal type": "spider",
    "name": "pauk",
    "owner": "Sasha",
    }
pets.append(pet)

for pet in pets:
    print("\nGet to know " + pet["name"].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))