with open("text_file.txt", "r") as file:
    y = file.readline()
    my_text = y.split()
    print(my_text)

for word in my_text:
    word_1 = word[::-1]
    if word in my_text and word_1 in my_text:
        print(word, word_1)
    else: pass
