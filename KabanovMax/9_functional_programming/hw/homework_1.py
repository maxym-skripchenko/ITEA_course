def present_simple(verb):
    endings = ("s", "ss", "x", "z", "ch", "sh")
    if verb.endswith(endings):
        return verb + "es"
    elif verb.endswith("y"):
        return verb[:len(verb) - 1] + "ies"
    else:
        return verb + "s"


print(present_simple("try"))
print(present_simple("brush"))
print(present_simple("run"))
