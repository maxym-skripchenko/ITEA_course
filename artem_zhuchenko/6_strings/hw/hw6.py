'''Write a program that maps a list of words into a list
of integers representing the lengths of the correponding words.'''


def words_to_integers(list_of_words):
        for word in list_of_words:
            return [len(word) for word in list_of_words]



