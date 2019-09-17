class Pet:
    dog = []

    def __init__(self, dog):
        self.dogs = dog

    def dog_hunger(self):
        hunger = False
        for dog in self.dog:
            if dog.is_hungry:
                hunger = True
        if hunger:
            print("my dogs are hungry")
        else:
            print("My dogs are not hungry")


my_dog = ['Shepard']
my_pets = Pet(my_dog)

print(my_pets.dog_hunger())
