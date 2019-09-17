from collections import Counter

with open("2nd_example.txt") as file:
    count = Counter(word for line in file for word in line.split())

print(count.most_common(5))
print("End of program")
