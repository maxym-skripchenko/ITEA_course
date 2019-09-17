str = input("write something: ")
nums,letters = 0,0
for i in str:

    if i.isdigit():
        nums+=1
    elif i.isalpha():
        letters+=1

print(letters, nums)