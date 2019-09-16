def overlapping(input_list_1, input_list_2):
    print(input_list_1)
    print(input_list_2)

    for item_1 in range(len(input_list_1)):
        for item_2 in range(len(input_list_2)):
            if input_list_1[item_1] == input_list_2[item_2]:
                return True


list_1 = ['aa', 'bb', 'cc']
list_2 = ['cc', 'dd', 'ee']

if overlapping(list_1, list_2):
    print("Overlapping")
else:
    print("No overlapping")
