num = [1,2,3,4,6,7,9,3]
chet = 0
nechet = 0
for i in num:
    if int(i) % 2 ==0:
        chet += 1
    else:
        nechet += 1
print(f'Четных чисел - {chet}, а нечетных - {nechet}')