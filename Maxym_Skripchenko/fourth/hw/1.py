user_input = input("Input your string: ")
alpha = 0
digit = 0
for i in user_input:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        continue

print(f"Number of digits: {digit}, number of letters: {alpha}")