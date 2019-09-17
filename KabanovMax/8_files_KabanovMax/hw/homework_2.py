from collections import Counter

with open("text") as file:
    count = Counter(word for line in file for word in line.split())

print(count.most_common(5))