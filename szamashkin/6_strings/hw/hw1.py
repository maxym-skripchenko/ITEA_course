def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
words = ['Petya', 'A', 'is not here']
print(map_to_lengths_for(words))
