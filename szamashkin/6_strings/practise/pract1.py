def generate_n_chars(n, c):
    string = ""
    for num in range(n):
        string += c
    return string

print(generate_n_chars(12, "x"))
print(generate_n_chars(10, "21"))
print(generate_n_chars(2, "Key"))