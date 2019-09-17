'''1. According to Wikipedia, a semordnilap is a word or phrase that spells
a different word or phrase backwards. ("Semordnilap" is itself
"palindromes" spelled backwards.)
Write a semordnilap recogniser that accepts a file name (pointing to a list of words)
from the program arguments and finds
and prints all pairs of words that are semordnilaps to the screen.
For example, if "stressed" and "desserts" is part of the word list, the
the output should include the pair "stressed desserts". Note, by the way,
that each pair by itself forms a palindrome!'''

import sys
sys.argv

file_name = sys.argv[1]

def semordnilap_recognizer(file_name):
    word_list_from_file = []
    with open(file_name, "r") as file:
        file_content = file.readlines()
        for word_line in file_content:
            word_line = word_line.strip()
            word_list_from_file.append(word_line)
    pairs = set()
    for word in word_list_from_file:
        palindromed_word = word[::-1]
        if palindromed_word in word_list_from_file:
            pairs.add(palindromed_word)
            pairs.add(word)
    return (pairs)

print(semordnilap_recognizer(file_name=file_name))