def max_number(number_1, number_2):
    if number_1 > number_2:
        print("The biggest name is ", number_1)
        return number_1
    elif number_2 > number_1:
        print("The biggest name is ", number_2)
        return number_2
    else:
        print("The numbers are the same")
        return

max_number(1, 4)
# max_number (number_1 = int(input("Enter the first number :")), number_2 = int(input("Enter the second number :")))