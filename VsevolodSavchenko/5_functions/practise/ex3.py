def is_vowel(char):
    vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y")
    if char not in vowels:
        print("False")
        return False
    else:
        print("True")
        return True

is_vowel("E")
is_vowel("a")
is_vowel("b")