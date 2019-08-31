def max_in_list(list):
  max = 0
  for n in list:
    if n > max:
      max = n
  return max

print(max_in_list([1,2,3,4,5,6,7,8,8,9,10]))
print(max_in_list([290,2,3,4]))
print(max_in_list([9,2,3,4,19]))