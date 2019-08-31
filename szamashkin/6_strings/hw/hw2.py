def find_longest_word(words):
    longest = ""
    for word in words:
        if len(word) >= len(longest):
            longest = word
    return longest
print(find_longest_word(["i", "am", "pythoning"]))
print(find_longest_word(["hello", "Ukraine"]))