def length_list(a,b):
    k=0
    while k < len(a):
        b.append(len(a[k]))
        k += 1
    return b

lists = ["grub","linux","fuck","tyccon"]
words = []
print(length_list(lists,words))