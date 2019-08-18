def my_is_member(my_list, element):
    for i in my_list:
        if i == element:
            return True
    return False
print(my_is_member (["j", "e", "a", "hg"], "aw"))