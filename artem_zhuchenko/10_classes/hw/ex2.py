'''Add a walk() method to Pets, Dog and Cats classes so that when you call the method on the Pets class,
each dog or cat instance assigned to the Pets class will walk(). Start by implementing the method in the
same manner as the speak() method. As for the method in the Pets class, you will need to iterate through
the list of dogs, then call the method itself.
'''


class Pets:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

# Rather than creating a list, I'd prefer to use classmethod to make them all walk:

    def walk(cls):
        cls.walks = True
        return "Pets are walking!"

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def eat(self):
        self.is_hungry = False
        return (f"{self.name} says Yummy!")


class Cat(Pets):

    def all_cats_walk(cls):
        cls.walks = True
        return "Cats are walking!"

    def this_cat_walks(self):
        self.walks = True

    def speak(self, sound="Miaw"):
        return "{} says {}".format(self.name, sound)


class Dog(Pets):

    def all_dogs_walk(cls):
        cls.walks = True
        return "Dogs are walking!"

    def this_dog_walks(self):
        self.walks = True
        return f"{self.name} is walking!"

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


scooby = Dog("Scooby", 2)
doo = Dog("Doo", 2)


print(Pets.walk(Pets))
pass

