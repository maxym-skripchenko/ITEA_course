def my_sum(numbers):
    total = 0
    for item in numbers:
        total += item
    return total

def my_multiply(numbers):
    total = 1
    for item in numbers:
        total *= item
    return total

print(my_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(my_multiply([1, 2, 3, 4, 5, 6, 7, 8, 9]))