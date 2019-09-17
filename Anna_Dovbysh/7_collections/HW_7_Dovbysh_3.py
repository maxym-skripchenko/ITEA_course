my_list = list(range(11))
print(my_list)

def first_in_list(my_list):
    return my_list[:3]
print(first_in_list(my_list))

def last_in_list(my_list):
    return my_list[-3:]
print(last_in_list(my_list))

def rev_list(my_list):
    return my_list[::-1]
print(rev_list(my_list))

def find_middle(my_list):
    middle = (len(my_list))/2
    if middle % 2 != 0:
        return my_list[int(middle)]
    pass
print (find_middle(my_list))