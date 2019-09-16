class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


class Dog:

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


my_dogs = [
    Sobaken("Pes", 6),
    Sobaken_2("Pes2", 9),
    Dog("Pes3", 29)
]

my_pets = Pets(my_dogs)

print("I have {} dogs.".format(len(my_pets.dogs)))
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
