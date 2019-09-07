class Dog:
    def __init__(self, name='Good boy', is_hungry=False, walk=False):
        self.is_hungry = is_hungry
        self.name = name
        self.walk = walk

    def eat(self):
        self.is_hungry = True

    def __str__(self):
        return f'{self.name} is hungry = {self.is_hungry}, and He had a walk({self.walk})'


class Cat:
    def __init__(self, name='Senya',  is_hungry=False, walk=False):
        self.is_hungry = is_hungry
        self.name = name
        self.walk = walk

    def eat(self):
        self.is_hungry = True

    def __str__(self):
        return f'{self.name} is hungry = {self.is_hungry}, and He had a walk({self.walk})'

    def walk_bool(self):
        self.walk = True


# def walking(list_):
#
#     for i in list_:
#         i.


class Pet:

    instances = [Cat('John'), Dog('Valentine'), Cat(), Dog()]

    def __init__(self, name='animal', is_hungry=False):
        self.is_hungry = is_hungry
        self.name = name

    def eat(self):
        self.is_hungry = True

    def walk(self):
        for i in self.instances:
            i.walk = True
            print(i)



if __name__=='__main__':

    # a = Dog()
    # print(a)
    # a.eat()
    # # walking_pet = Pet().instances.walk
    # print(Pet().walk())
    a = Cat()
    a.eat()
    breakpoint()
    print(a)
