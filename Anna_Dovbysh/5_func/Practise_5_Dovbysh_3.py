def vowel_or_not(my_string):
    #my_string = str(input())
    for vow in my_string:
        if vow in 'aeiou':
            vow = True
        else: vow = False
        return print(vow)


vowel_or_not(input('info - '))

