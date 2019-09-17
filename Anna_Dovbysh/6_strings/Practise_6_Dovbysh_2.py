def is_palindrome(word):
    word_1 = word[::-1]
    if word == word[::-1]: print(True)
    else: print(False)
    return (word)

#is_palindrome('radar')