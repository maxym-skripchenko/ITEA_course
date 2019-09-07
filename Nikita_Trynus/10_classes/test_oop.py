import sys
sys.path.append(r'/Users/nicktrynus/ITEA/ITEA_course/Nikita_Trynus/10_classes/hw/')
import classssses as postav_me_100_v_sertificate


def test_instance():
    a = postav_me_100_v_sertificate.Dog()
    assert isinstance(a,postav_me_100_v_sertificate.Dog)

def test_output():
    a = postav_me_100_v_sertificate.Dog()
    assert str(a) == 'Good boy is hungry = False, and He had a walk(False)'


def test_eat():
    a = postav_me_100_v_sertificate.Cat()
    a.eat()
    assert str(a) == 'Senya is hungry = True, and He had a walk(False)'
