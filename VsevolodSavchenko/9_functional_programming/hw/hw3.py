import re
import time


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print("Время выполнения функции: %f" % (time.time()-t))
        return res

    return tmp


@timer
def make_3sg_form(verb):
    es = ("o", "ch", "s", "sh", "x", "z")
    if verb.endswith("y"):
        return re.sub("y$", "ies", verb)
    elif verb.endswith(es):
        return verb + "es"
    else:
        return verb + "s"


print(make_3sg_form("try"))
print(make_3sg_form("go"))
print(make_3sg_form("catch"))
print(make_3sg_form("fix"))
print(make_3sg_form("begin"))
