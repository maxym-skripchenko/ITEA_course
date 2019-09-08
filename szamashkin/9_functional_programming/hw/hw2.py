vowels = "aeiou"
cons = "bcdfghjklmnpqrstvwxyz"

def make_ing_form(verb):
    l = len(verb)

    if verb.endswith('ie'):
        return verb[:l - 2] + 'ying'
    elif verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee']:
        return verb[:l - 1] + 'ing'
    elif verb[l-1] in cons and verb[l-2] in vowels and verb[l-3] in cons:
        return verb + verb[l-1] + 'ing'
    else:
        return verb + 'ing'

# test
print(make_ing_form('lie'))
print(make_ing_form('see'))
print(make_ing_form('hug'))
print(make_ing_form('move'))