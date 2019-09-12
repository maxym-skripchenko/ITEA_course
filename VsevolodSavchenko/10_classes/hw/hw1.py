class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    cats = []

    def __int__(self, cats):
        self.cats = cats


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def eat(self):
        self.is_hungry = False


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def eat(self):
        self.is_hungry = False


class Sobaken(Dog):
    pass


class Sobaken_2(Dog):
    pass


class Kotyara(Cat):
    pass


class Kotyara_2(Cat):
    pass


my_animals = [
    Sobaken("Pes", 6),
    Sobaken_2("Pes2", 9),
    Kotyara("Kot", 1),
    Kotyara_2("Kot2", 2)
]

my_pets = Pets(my_animals)
print("I have {} animals.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}.".format(dog.name, dog.age))

are_my_dogs_hungry = True
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_dogs_hungry = True
if are_my_dogs_hungry:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

are_my_cats_hungry = False
for cat in my_pets.cats:
    if cat.is_hungry:
        are_my_cats_hungry = True
if are_my_cats_hungry:
    print("My cats are hungry.")
else:
    print("My cats are not hungry.")
