vowels = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"


def make_ing_form(verb):
    a = len(verb)
    if verb.endswith('ie'):
        return verb[:a - 2] + 'ying'
    elif verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee']:
        return verb[:a - 1] + 'ing'
    elif verb[a - 1] in cons and verb[a - 2] in vowels and verb[a - 3] in cons:
        return verb + verb[a - 1] + 'ing'
    else:
        return verb + 'ing'


print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('hug'))
print(make_ing_form('move'))
