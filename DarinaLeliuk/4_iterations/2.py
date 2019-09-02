series=[2, 3, 4, 5, 7, 11, 22]
counteven=0
countodd=0
for myelement in series:
    if myelement % 2 != 0:
        counteven += 1
    elif myelement % 2 == 0:
        countodd +=1
print(countodd)
print(counteven)