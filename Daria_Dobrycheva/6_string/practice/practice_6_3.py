def overlapping(inputList1, inputList2):
    print(inputList1)
    print(inputList2)

    for i in range(len(inputList1)):

        for j in range(len(inputList2)):

            if inputList1[i] == inputList2[j]:
                return True


List1 = ['aa', 'bb', 'cc']
List2 = ['cc', 'dd', 'ee']

if overlapping(List1, List2) == True:
    print("Overlapping")
else:
    print("No overlapping")