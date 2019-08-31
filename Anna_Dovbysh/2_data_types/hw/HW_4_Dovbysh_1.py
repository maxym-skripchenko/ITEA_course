user_input = input('Input : ')
i=0
j=0
for element in user_input:
    if element.isdigit():
        i +=1
    elif element.isalpha():
        j +=1
print(i)
print(j)