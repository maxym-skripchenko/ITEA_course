from collections import Counter

with open("example_for_hw2.txt") as file:
    count = Counter(word for line in file for word in line.split())

print(count.most_common(5))
