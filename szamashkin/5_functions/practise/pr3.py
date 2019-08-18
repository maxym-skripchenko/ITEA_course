def my_vowel(element):
    vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U", "y", "Y")
    if element in vowels:
        print("True")
        return True
    else:
        print("False")
        return False
my_vowel("sss")
my_vowel("g")
my_vowel("A")