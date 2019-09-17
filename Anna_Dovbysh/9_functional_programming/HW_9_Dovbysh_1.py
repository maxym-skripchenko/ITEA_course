def make_3sg_form(my_string):
    for word in my_string:
        if word[-1] == 'y':
            word = word.replace('y','ies')
        elif word.endswith('o') or word.endswith('s') or word.endswith('ch') or word.endswith('sh') or word.endswith('x') or word.endswith('z'):
            word = word + 'es'
        else: word = word + 's'
    return word


#my_string = 'run', 'try', 'brush', 'fix', 'go'
#make_3sg_form(my_string)

