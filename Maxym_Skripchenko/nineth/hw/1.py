def make_3gs_form(word):
    if word.endswith("y"):
        return word[0:len(word)-1] + "ies"
    elif word.endswith("o") or word.endswith("ch") or word.endswith("s") or word.endswith("sh") or word.endswith("x") or word.endswith("z"):
        return word + "es"
    else:
        return word + "s"

p = input("Input your word: ")
print(make_3gs_form(p))