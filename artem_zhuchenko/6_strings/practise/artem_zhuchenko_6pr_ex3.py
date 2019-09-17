'''Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
you should (also) write it using two nested for-loops.'''

# def overlapping(list1, list2):
#     for a in range(len(list1)):
#         for b in range(len(list2)):
#             if a == b:
#                 return True
#             else:
#                 return False


list_a = [9, 8, 7]
list_b = [5, 8, 0]

# print(overlapping(list_a, list_b))

def overlapping(list1, list2):
    for element in list1:
        while element:
            for element_2 in list2:
                if element == element_2:
                    return True
                else:
                    return False




print(list_a)
print(list_b)
print(overlapping(list_a, list_b))