def inging(word):
    if word.endswith("ie"):
        return  word[0:len(word)-2] + "ying"
    elif word.endswith("e"):
        return word[0:len(word)-1] + "ing"
    else:
        return word + "ing"

p = input("Input your word: ")
print(inging(p))