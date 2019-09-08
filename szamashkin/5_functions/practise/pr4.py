def my_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total
print(my_sum([1, 2, 3, 4, 7, 9, 89, 5634, 765]))

def my_multiply(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total
print(my_multiply([1, 2, 3, 4, 7, 9, 89, 5634, 765]))