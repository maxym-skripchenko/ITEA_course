amount  = int(input("Enter num: "))
odd = 0
even = 0
for i in range(amount+1):

    if i % 2:

        odd += 1

    else:

        even += 1

print(even, odd)        