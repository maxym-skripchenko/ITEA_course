from hw3 import timer

def is_vowel(char):
    vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y")
    if char not in vowels:
        return False
    else:
        return True

@timer
def make_ing_form(verb):
    if verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif verb.endswith('e') and (verb[-2].endswith('e') or len(verb) == 2):
        return verb + 'ing'
    elif verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif not is_vowel(verb[-1]) and is_vowel(verb[-2]) and not is_vowel(verb[-3]):
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'


if __name__ == "__main__":
    print(make_ing_form("make"))
    print(make_ing_form("move"))
    print(make_ing_form("likE"))
    print(make_ing_form("agree"))
    print(make_ing_form("hit"))
