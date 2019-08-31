import re
import datetime


pat = re.compile('[qwrtypsdfghjklzcvbnm][euoai][qwrtypsdfghjklzcvbnm]')


def time_func(func):

    def wrapper(string):

        time_start = datetime.datetime.now()
        result = func(string)
        print(datetime.datetime.now() - time_start)
        return result

    return wrapper

# @time_func
def make_3sg_form(string):

    if string:

        if string.endswith(('o', 'ch', 's', 'sh', 'x', 'z')):

            return string + 'es'

        elif string.endswith('y'):

            return string[:-1] + 'ies'

        else:

            return string + 's'

    else:

        return 'Може шо то надо ввести'

# @time_func
def make_ing_form(string):

    if string:

        if pat.fullmatch(string.strip()):

            return string + string[-1] + 'ing'

        elif string.endswith('ie'):

            return string[:-2] + 'ying'

        elif string.endswith('e'):

            if string.endswith('ee'):
                return string + 'ing'

            else:
                return string[:-1] + 'ing'

        else:

            return string + 'ing'

    else:

        return 'Може шо то надо ввести'


test1 = ['try', 'brush', 'run', 'fix','']
test2 = ['lie', 'see', 'move', 'hug']


if __name__ == '__main__':

    for word in test2:

        print(make_ing_form(word))


