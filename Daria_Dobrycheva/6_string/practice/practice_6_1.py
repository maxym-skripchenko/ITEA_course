def generate_n_charts(x, y):
    text = ""
    incorrect = 0
    while x > 0:
        text += y
        text += " "
        x -= 1
    return text

a = int(input("How many times a word? "))
b = input("What word? ")

povtor = generate_n_charts(a, b)
print(povtor)