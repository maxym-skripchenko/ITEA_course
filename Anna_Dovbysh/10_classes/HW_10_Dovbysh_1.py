class Animals:
    is_hungry = True
    def __init__(self, my_type, name):
        self.my_type = my_type
        self.name = name

    def eat(self):
         print(f'Your fed the animals, {self.name} is not hungry')
         self.is_hungry = False

Tomas = Animals('Cat', 'Tomas')
Sharik = Animals('Dog', 'Sharik')
Kesha = Animals('Parrot', 'Kesha')

Tomas.eat()
Sharik.eat()
