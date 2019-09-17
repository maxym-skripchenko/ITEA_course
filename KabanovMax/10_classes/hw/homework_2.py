class Pet:

    def __init__(self, dog):
        self.dogs = dog

    def dog_counter(self):
        return "I have {} dogs".format(len(self.dogs))

    def dog_age(self):
        for animal in self.dogs:
            print("{} is {} years old".format(animal.name, animal.age))

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

    def walk(self):
        return "{} is walking ".format(self.name)


class Corgi(Dog):
    pass


class German_Shepard(Dog):
    pass


class Pug(Dog):
    pass


class Duchshund(Dog):
    pass


my_dogs = [Corgi("Shepard", 3), German_Shepard("Vulkan", 5), Pug("Keks", 1), Duchshund("Bullet", 7)]
my_pets = Pet(my_dogs)
print(my_pets.dog_counter())
print(my_pets.walk())
