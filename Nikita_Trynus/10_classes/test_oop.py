from hw.classssses import Cat, Dog


def test_instance():
    a = Dog()
    assert isinstance(a,Dog)

def test_output():
    a = Dog()
    assert str(a) == 'Good boy is hungry = False, and He had a walk(False)'


def test_eat():
    a = Cat()
    a.eat()
    assert str(a) == 'Senya is hungry = True, and He had a walk(False)'
