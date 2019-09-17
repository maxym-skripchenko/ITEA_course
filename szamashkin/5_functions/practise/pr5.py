
#def my_function(name, country="Ukraine"):
#   print(f"My name is: {name}")



def power(x, y):
    result = x**y
    return result

x = 2
y = 3

power_of_x_y = power(x, y)
print(power_of_x_y)

def my_is_member(my_list, element):
    for i in my_list:
        if i == element:
            return True
    return False
print(my_is_member (["j", "e", "a", "hg"], "aw"))

