class Pets(type):
    def __new__(cls, *a, **kw):
        cls.all = set()
        return type.__new__(cls, *a, **kw)

    def __iter__(cls):
        return cls.all.__iter__()

    def add(cls, e):
        cls.all.add(e)

    def discard(cls, e):
        cls.all.discard(e)


class Cat(metaclass=Pets):

    def __init__(self, name, age):
        self.__class__.add(self)
        self.name = name
        self.age = age
        self.walk = False

    def make_cat_walk(self):
        self.walk = True
        return "Pets are walking!"


matroskin = Cat("Matroskin", 12)
matroskin2 = Cat("Matroskin2", 13)

for cat in Cat:
    cat.make_cat_walk()
pass

