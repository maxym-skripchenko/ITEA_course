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