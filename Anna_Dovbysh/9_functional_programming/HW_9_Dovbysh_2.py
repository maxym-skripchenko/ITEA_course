def make_ing_form(my_string):
#vowel = 'a', 'e', 'i', 'o', 'u'
    for word in my_string:
        if word.endswith('ie'):
            word = word.replace('ie','y') + 'ing'
            print(word)
        elif word.endswith('e') and word not in ('be', 'see', 'flee', 'knee'):
            word = word.replace('e','ing', 1)
            print(word)
        elif word[-1] not in ('a', 'e', 'i', 'o', 'u') and word[-2] in ('a', 'e', 'i', 'o', 'u') and word[-3] not in ('a', 'e', 'i', 'o', 'u'):
            word = word + word[-1] + 'ing'
            print(word)
        else: word = word + 'ing'
        print(word)
    return word


my_string = 'lie', 'see', 'move', 'hug', 'go'
make_ing_form(my_string)

