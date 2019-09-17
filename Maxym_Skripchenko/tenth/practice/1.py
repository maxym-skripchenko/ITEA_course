class Dog:
    def __init__(self, age,name):
        self.age = age
        self.name = name

    def description(self):
        return "{} "

def get_biggest_number(l):
    max = d1.age
    for i in dlist:
        if i.age > max:
            max = i.age
        else:
            continue
    return print(f"The oldest dog is {i.name}, and its age is {i.age}")


d1 = Dog(2, "Pam")
d2 = Dog(1, "Rocky")
d3 = Dog(5, "Honey")

dlist = [d1,d2,d3]
get_biggest_number(dlist)