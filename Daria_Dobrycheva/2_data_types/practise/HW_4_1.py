sample = input("somthing") #sample string
for element in sample:
    if element.isdigit():
        print("{0} is digit".format(element))
    elif element.isalpha():
        print("{0} is alpha".format(element))



