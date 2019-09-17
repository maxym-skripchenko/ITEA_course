'''3. Write a function filter_long_words() that takes a list
of words and an integer n and returns the list of words that
are longer than n.'''

def filter_long_words(list_of_words, number_of_characters_to_pass):
    list_of_long_words = []
    for word in list_of_words:
        if len(word) > number_of_characters_to_pass:
            list_of_long_words.append(word)
    if list_of_long_words == []:
        return None
    else:
        return list_of_long_words

print(filter_long_words([], 4))