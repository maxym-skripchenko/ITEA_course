def filter_long_words(words, n):
    return [word for word in words if len(word) > n]


print(filter_long_words(["qaz", "Hello, World", "TEST"], 3))