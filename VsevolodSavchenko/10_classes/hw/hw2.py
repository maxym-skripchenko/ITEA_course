class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

    cats = []

    def __int__(self, cats):
        self.cats = cats

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

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "%s is walking!" % self.name


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "%s is walking!" % self.name


class Sobaken(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


class Sobaken_2(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


class Kotyara(Cat):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


class Kotyara_2(Cat):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)


my_animals = [
    Sobaken("Pes", 6),
    Sobaken_2("Pes2", 9),
    Kotyara("Kot", 1),
    Kotyara_2("Kot2", 2)
]

my_pets = Pets(my_animals)
my_pets.walk()
