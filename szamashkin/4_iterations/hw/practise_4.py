#####
list_numbers = [1,2,3,4,5,6,7,8,9]   # Create list numbers
#print(list_numbers)
list_numbers2 = []
for element in list_numbers:
#  print(element)
    if element == 3 or element == 6:
        continue
    elif element > 6:
        break
    print(element)
    list_numbers2.append(element)
print(list_numbers2)

#####
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
print("Number of even numbers :", count_even)
print("Number of odd numbers :", count_odd)

#####
while True:
    a = input("inp: ")
    if not a:
        break
    print(a.lower())