'''2. Write a function find_longest_word() that takes
a list of words and returns the length of the longest one.'''


def find_longest_word(list_of_words):
    for word in list_of_words:
       list_with_lenghts_of_words = [len(word) for word in list_of_words]
    return max(list_with_lenghts_of_words)



