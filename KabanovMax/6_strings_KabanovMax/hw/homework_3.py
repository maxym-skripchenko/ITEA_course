def filter_longest_words(words, number):
    return [word for word in words if len(word) > number]

print(filter_longest_words(["qwerty", "Corgi is the best dog", "something"], 10))