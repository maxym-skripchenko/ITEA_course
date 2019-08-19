def length(my_list):
    counter = 0
    for counter in my_list[:]:
        counter += 1
    print(counter)
    return (counter)

length([1,2,2])
