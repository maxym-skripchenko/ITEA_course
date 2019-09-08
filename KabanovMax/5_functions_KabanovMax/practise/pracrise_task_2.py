def my_length(string):
    count = 0
    for item in string:
        count = count + 1
    print(count)
    return count

my_length(input("Print some thing: "))