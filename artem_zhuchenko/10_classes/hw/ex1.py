'''Add for each class (Dog, Cat, etc.) attribute is_hungry = True Then add a method called eat()
which changes the value of is_hungry to False when called. Create three instance of each class
and call eat method.
'''


class Pets:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def eat(self):
        self.is_hungry = False
        return (f"{self.name} says Yummy!")

class Cat(Pets):

    def speak(self, sound="Miaw"):
        return "{} says {}".format(self.name, sound)


class Dog(Pets):

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

class Hamster(Pets):

    def run(self, speed):
        return f"{self.name} runs {speed}!"


class RussellTerrier(Dog):

    def run(self, speed):
        if speed in ("slow", "fast"):
            return "{} runs {}".format(self.name, speed)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    def description(self):
        return "{} is {} years old".format(self.name, self.age).upper()


class Dvorniaga(Bulldog, RussellTerrier):
    pass


murchik = Cat("Murchik", 8)

print(murchik.eat())

artem = Dog("Artem", 23)

print(artem.eat())

maska = Hamster("Maska", 2)

print(maska.run("fast"))

Tuzik = Dvorniaga("Tuzik", 5)

(Tuzik.eat())

