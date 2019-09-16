def semordnilap(name):
    word_list = []
    with open(name, "r") as file:
        file_content = file.readlines()
        for word_line in file_content:
            word_line = word_line.strip()
            word_list.append(word_line)
    pairs = set()
    for word in word_list:
        palindrom_word = word[::-1]
        if palindrom_word in word_list:
            pairs.add(palindrom_word)
            pairs.add(word)
    return pairs


print(semordnilap("words"))
