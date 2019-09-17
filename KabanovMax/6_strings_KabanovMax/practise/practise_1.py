def generate_n_chars(number, str):
    result = ""
    for item in range(number):
        result += str
    return result


print(generate_n_chars(3, "word"))
