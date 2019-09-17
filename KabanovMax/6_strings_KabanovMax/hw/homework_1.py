def number_lengths(items):
    lengths = []
    for letters in items:
        lengths.append(len(letters))
    return lengths

print(number_lengths(["qwerty", "Corgi is the best dog", "something"]))