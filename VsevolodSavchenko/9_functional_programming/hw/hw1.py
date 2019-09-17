import re
from hw3 import timer

@timer
def make_3sg_form(verb):
    es = ("o", "ch", "s", "sh", "x", "z")
    if verb.endswith("y"):
        return re.sub("y$", "ies", verb)
    elif verb.endswith(es):
        return verb + "es"
    else:
        return verb + "s"


if __name__ == "__main__":
    print(make_3sg_form("try"))
    print(make_3sg_form("go"))
    print(make_3sg_form("catch"))
    print(make_3sg_form("fix"))
