class Pet:

    def __init__(self, dogs):
        self.dogs = dogs

    def dogs_counter(self):
        return "I have {} dogs".format(len(self.dogs))

    def dogs_age(self):
        for animal in self.dogs:
            print("{} is {} years old".format(animal.name, animal.age))

    def dogs_hunger(self):

        are_my_dogs_hungry = False
        for dog in self.dogs:
            if dog.is_hungry:
                are_my_dogs_hungry = True
        if are_my_dogs_hungry:
            print("my dogs are hungry")
        else:
            print("My dogs are not hungry")

    def walk(self):
        for dog in self.dogs:
            print("{} is walking".format(dog.name))


class Dog:

    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def hungry_statement(self):
        if not self.is_hungry:
            return "my dogs are not hungry"
        else:
            return "my dogs are hungry"

    def walk(self):
        return "{} is walking ".format(self.name)


class Mops(Dog):
    pass


class Chihuahua(Dog):
    pass


my_dogs = [Mops("sobaka", 5), Chihuahua("roxy", 3), Dog("sharik", 7), Chihuahua("bimba", 9)]
my_pets = Pet(my_dogs)
print(my_pets.dogs_counter())
print(my_pets.dogs_hunger())
print(my_pets.dogs_age())
print(my_pets.walk())
print(my_dogs[0].walk())
