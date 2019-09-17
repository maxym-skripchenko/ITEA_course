class Pet:

    instances = []

    def __init__(self,  name='animal', is_hungry=False):
        self.is_hungry = is_hungry
        self.name = name
        self.instances

    def eat(self):
        self.is_hungry = True

    def walk(self):
        for i in self.instances:
            i.walk = True
            print(i)


all_pets_on_the_street = Pet()


class Dog:
    def __init__(self, name='Good boy', is_hungry=False, walk=False):
        self.is_hungry = is_hungry
        self.name = name
        self.walk = walk
        all_pets_on_the_street.instances.append(self)

    def eat(self):
        self.is_hungry = True

    def __str__(self):
        return f'{self.name} is hungry = {self.is_hungry}, and He had a walk({self.walk})'


class Cat:
    def __init__(self, name='Senya',  is_hungry=False, walk=False):
        self.is_hungry = is_hungry
        self.name = name
        self.walk = walk
        all_pets_on_the_street.instances.append(self)

    def eat(self):
        self.is_hungry = True

    def __str__(self):
        return f'{self.name} is hungry = {self.is_hungry}, and He had a walk({self.walk})'

    def walk_bool(self):
        self.walk = True

class Pet_init:

    instances = []

    def __init__(self, cat, dog, name='animal', is_hungry=False):
        self.is_hungry = is_hungry
        self.name = name
        self.instances.append(cat).append(dog)

    def eat(self):
        self.is_hungry = True

    def walk(self):
        for i in self.instances:
            i.walk = True
            print(i)


if __name__ == '__main__':

    cat = Cat()
    dog = Dog()
    print(all_pets_on_the_street.instances)
    print(Cat(), Dog(), " Yura postavb 100 pleeeeeaaaseeeee")
