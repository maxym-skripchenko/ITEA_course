list_numbers = [1,2,3,4,5,6,7,8,9]   # Create list numbers

#for element in list_numbers:
 #   if (element % 2) == 0:
  #      print("{0} is Even number".format(element))
   # else:
    #    print("{0} is Odd number".format(element))


#num = int(input("Enter a number: "))
#if (num % 2) == 0:
#    print("{0} is Even number".format(num))
#else:
#    print("{0} is Odd number".format(num))

#counter = list_numbers
list_even = []
list_odd = []
for element in list_numbers:
    if (element % 2) == 0:
        list_even.append(element)
        print(list_even)
    else:
        list_odd.append(element)
        print(list_odd)