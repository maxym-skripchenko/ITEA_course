class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def walk(self):
        return "%s is walking!" % (self.name)


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
my_pets.walk()
