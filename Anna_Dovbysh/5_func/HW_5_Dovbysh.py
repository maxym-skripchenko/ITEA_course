def my_max_in_list(my_list):
    my_max = 0
    for i in my_list:
        if i > my_max:
            my_max = i
    print(my_max)
    return (my_max)

my_max_in_list([1,10,3])
