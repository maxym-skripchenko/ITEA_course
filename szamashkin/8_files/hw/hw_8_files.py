def is_semordnilap(filename):
    file = open(filename)
    words = file.read().split()
    results = []
    for word1 in words:
        for word2 in words:
            if word1 == word2[::-1]:
                results.append(word1)
    return results


if __name__ == "__main__":
    print(is_semordnilap('example_for_hw_8_files.txt'))
