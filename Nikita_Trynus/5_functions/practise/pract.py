
vowel = 'euoai'

def max(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    return a if a > b else b


def length(lis):

    count = 0
    for i in lis:

        count += 1

    return count


def is_vowel(c):

     return True  if c in vowel else False


def sum(lis):

    summ = 0
    for i in lis:

        summ+=i

    return summ


def mult(lis):
    summ = 1
    for i in lis:
        summ *= i

    return summ

def is_member(a,lis):

    for i in lis:

        if i == a:

            return True

    return False


def overlapping(a,b):

    return True if set(a).intersection(set(b)) else False




print(max(1,2), length('11111'), is_vowel('a'), sum([1, 2, 3, 4]), mult([1, 2, 3, 4]), is_member(1,[12]),\
       overlapping('abc','bdkd') )
