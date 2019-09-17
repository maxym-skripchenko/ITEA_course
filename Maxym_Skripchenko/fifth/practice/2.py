def my_len(a):
    count = 0
    for i in a:
        count += 1
    return count

b = [1,2,3,4]
c = "lol"
print(my_len(b))
print(my_len(c))