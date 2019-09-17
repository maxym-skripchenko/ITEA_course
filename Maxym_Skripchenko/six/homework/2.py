def find_longest_word(a):
    longest = len(a[0])
    for i in a:
        if len(i) > longest:
            longest = len(i)
        else:
            continue
    return longest

lists = ["a","ab","abb","b","baab"]
print(find_longest_word(lists))
