'''2. Write a Python program to count the number of even
and odd numbers from a series of numbers.'''


my_tuple2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)   #setting tuple
odd_count = 0                                            #setting variables to count odd and even nubmers
even_count = 0
for element in my_tuple2:
   if element % 2 == 0:
    even_count += 1
   else:
    odd_count += 1
print(odd_count)
print(even_count)

