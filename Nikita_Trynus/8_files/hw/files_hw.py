import sys
import pandas as pd
from collections import Counter
import collections

def rec(str1,str2):

    if str1==str2[::-1]:
        return f'{str1} and {str2}'

    else:
        return None


def recogniser(file):

    for word in file:

        for semor in file:

            if word == semor[::-1]:

                print(f'{word} and {semor}')


            else:
                continue

    pass


# def pannnda(df):

def my_strip(string):
    return string.strip(' -:=()_\n\t[].,')

if __name__=='__main__':
    #/Users/nicktrynus/PycharmProjects/Python_leraning/word.txt
    # word.txt
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    # semord = open(f'{sys.argv[1]}', 'r')
    pep = open('pep.txt', 'r')
    pep_filter = list(map(my_strip,pep.readlines()))
    key_value = Counter(pep_filter)
    count = 0
    for key, value in sorted(key_value.items(), key=lambda item: item[1], reverse=True):
        if count == 0:
            count += 1
            continue

        if count < 6:
            print("%s: %s" % (key, value))
            count += 1

        else:

            break

    # filter1 = list(map(my_strip,semord.readlines()))
    # recogniser(filter1)

    # a = (pd.DataFrame(semord, columns=['Words']).apply(lambda row: my_strip(row['Words']), axis=1))
    # print(a.isin(['aa']))
