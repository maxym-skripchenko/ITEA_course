def vowel(a, b):
    if a in b:
        return True
    else:
        return False


vowels = ["a", "e", "i", "o", "u"]
letter = input("Input a letter: ")
print(vowel(letter, vowels))