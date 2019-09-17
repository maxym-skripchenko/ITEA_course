list = [2,2,2,2]

while True:
    print("Input your number: ")
    list.append(int(input()))
    loop_breaker = input("Are you done? (y/n)")
    if loop_breaker == "y" or loop_breaker == "yes":
        break
    else:
        continue

odd = 0
even = 0

for i in list:
    if i % 2 == 0:
        odd += 1
    else:
        even += 1

print(f"Odd: {odd}, Even: {even}")