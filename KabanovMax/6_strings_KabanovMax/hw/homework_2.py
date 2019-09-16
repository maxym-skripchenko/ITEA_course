def longest_word(my_longest):
    return max(len(word) for word in my_longest.split())

print(longest_word("Corgi is the best dog"))