def my_overlapping(my_list_1,my_list_2):
    for element in my_list_1:
        if element in my_list_2:
            element = True
        else: element = False
    return print(element)

my_overlapping([1,2,4],[6,4,5])







