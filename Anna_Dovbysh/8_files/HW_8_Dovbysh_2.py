import re

i=0
frequency = {}
document_text = open('file_PEP.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    if frequency[words] > 0:
       i += 1
       if frequency[words] > i:
           print(words, frequency[words])
           sr = str(frequency[words])
           w = str(words)
with open("new_file.txt", "w") as file_write:
    file_write.write(sr)
