def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

print(map_to_lengths_for(["abcde", "Hello, World", "TEST"]))
