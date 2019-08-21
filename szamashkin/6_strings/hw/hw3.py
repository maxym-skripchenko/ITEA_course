def filter_long_words(x, n):
    result_set = []
    for i in x:
        if len(i) > n:
            result_set.append(i)
    return result_set
print(filter_long_words(['this','is','a','word'],1))