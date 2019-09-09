def make_3sg_form(verb):
    endings = ("o", "s", "x", "z", "ch", "sh")
    if verb.endswith("y"):
        return verb[:len(verb) - 1] + "ies"
    elif verb.endswith(endings):
        return verb + "es"
    else:
        return verb + "s"


print(make_3sg_form("try"))
print(make_3sg_form("brush"))
print(make_3sg_form("run"))
