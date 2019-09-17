class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} year old'

    def walk(self):
        return f'{self.name} is walk'

class Dog(Pets):
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

class Cat(Pets):
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

tomas = Cat('Tomas', 'one')
print(tomas.description())
print(tomas.walk())
print(tomas.speak('may may'))
