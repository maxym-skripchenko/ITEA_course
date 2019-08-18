# user_input = 0
# while True:
#     if user_input:
#         break
#     else:
#         user_input = input("Input smtng: ")

# counter = 10
# number_list = []
# while counter > 0:
#     if counter == 6:
#         number_list.append(counter)
#         continue
#     else:
#         counter -= 1
#         print(counter)

# list = [1,2,3,4]
# for element in list:
#     print(element)

# my_string = "Hello world!"
#
# for letter in my_string:
#     print(letter)

#
# my_tuple = (1,2,3,4)
# for element in my_tuple:
#     print(element)

# my_iter_string = "Hello World".split(' ')
# print(my_iter_string)
# print(next(my_iter_string))
# print(next(my_iter_string))
# print(next(my_iter_string))
# print(next(my_iter_string))
# print(next(my_iter_string))
# print(next(my_iter_string))

my_tuple = (1,2,3,4,5)

for element in my_tuple:
    if element == 2:
        print("Break clause")
        break
    elif element == 1:
        print("continue clause")
        continue
    print("We are there")
print("Next code")