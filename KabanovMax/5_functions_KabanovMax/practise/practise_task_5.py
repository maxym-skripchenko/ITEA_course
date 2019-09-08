def my_is_member(a, x):
    for item in a:
        if item == x:
            return True
    return False

print(my_is_member(["q", "w", "e", "rt"], "yu"))
print(my_is_member(["q", "w", "e", "rt"], "rt"))