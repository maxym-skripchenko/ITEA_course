
class Car:
    """
    fields:
        * Brand
        * Model
        * Color
        * Year
        * Engine volume
        * Odometer
        * Phone number
    """

    def __init__(self,brand = "Nothing", model = "Nothing", color= "Nothing", year= "Nothing", engine= "Nothing", volume = "Nothing", odometer= "Nothing",phone_number= "Nothing"):

        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.engine = engine
        self.volume = volume
        self.odometer = odometer
        self.phone_number = phone_number
        # return self

    def __str__(self):

        return f'{self.phone_number},{self.brand}, {self.color}, {self.engine}, {self.model}, {self.odometer}, {self.volume}, {self.year}'
fav = ["Lexus", "LX","Black"]
a = Car('a')
value = 100
a.brand = input('brand:')
if len(a.brand)>5 : value-=5
a.model = input('model:')
if len(a.model)>5 : value-=5
a.color = input('color:')
if len(a.color)>5 : value-=5
a.year = input('year:')
if len(a.year)>5 : value-=5
a.engine = input('engine:')
if len(a.engine)>5 : value-=5
a.volume = input('volume:')
if len(a.volume)>5 : value-=5
a.odometer = input('odometer:')
if len(a.odometer)>5 : value-=5
a.phone_number = input('phone_number:')
if len(a.phone_number)>5 : value-=5

if a.model not in fav:
    print(a.brand)

print(fav)

try: a.year = int(a.year)
except Exception as error:
    print(error)
else:
    print(a.year)

try: a.engine = float(a.engine) +0.1
except Exception as error:
    print(error)
else:
    print(a.engine)

a.odometer = int(a.odometer)
if a.odometer < 1000:
    print('good')
elif a.odometer >= 100000:
    value-=25
elif a.odometer > 50000:
    value-=10

if a.model in fav or a.model == 'BMW':
    if a.color in fav:
        if a.year < 5:
            value = 100
print(a, value)