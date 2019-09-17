def filter_longest_word(a,b,n):
    for i in a:
        if len(i) > n:
            b.append(i)
        else:
            continue
    return b

lists = ["bab","ab","laba","abab","retard"]
b = []
n = int(input("n = "))
print(filter_longest_word(lists,b,n))