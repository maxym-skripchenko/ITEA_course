def is_member(x, a):
    if len(a) == 0:
        return False
    return x == a[0] or is_member(x, a[1:])

print(is_member(1, [1, 11]))
print(is_member("a", ["a", 1]))
print(is_member("b", [1, 2, "a"]))