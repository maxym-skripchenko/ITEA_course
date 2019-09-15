def map_str_to_int(strl):

    a = []
    for i in strl:

        a.append(len(i))

    return a

def find_longest_word(strl):

    nums = map_str_to_int(strl)

    return max(nums)

def filter_long_words(strl, n):

    b = []
    for count,j in enumerate(strl):

        if len(j) >= n:

            b.append(j)

    return b

if __name__=='__main__':

    print(map_str_to_int(['1', '22','333']))
    print(find_longest_word(['1', '22','333']))
    print(filter_long_words(['1', '22','333'], 2))
