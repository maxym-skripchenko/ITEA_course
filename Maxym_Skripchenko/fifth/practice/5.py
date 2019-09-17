def my_len(a):
    count = 0
    for i in a:
        count += 1
    return count

def is_member(a,b, count):
    for counter,i in enumerate(a,0):
        if type(i) != type(b):
            return False
        else:
            if i == b:
                return True
            elif i != b and counter == count-1:
                return False
            else:
                continue


a = ["a", "d"]
b = "f"
count = my_len(a)
print(is_member(a,b,count))