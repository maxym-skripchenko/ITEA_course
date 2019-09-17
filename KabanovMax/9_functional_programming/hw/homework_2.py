consonant = "bcdfghjklmnpqrstvwxyz"
vowel = "aeiou"


def continuous(verb):
    lengths = len(verb)
    if verb.endswith('ie'):
        return verb[:lengths - 2] + 'ying'
    elif verb[lengths - 1] in consonant \
            and verb[lengths - 2] in vowel\
            and verb[lengths - 3] in consonant:
        return verb + verb[lengths - 1] + 'ing'
    elif verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee']:
        return verb[:lengths - 1] + 'ing'
    else:
        return verb + 'ing'


print(continuous('lie'))
print(continuous('see'))
print(continuous('hug'))
print(continuous('move'))
