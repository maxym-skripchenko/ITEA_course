def my_decorator(func):
    import time

    def time_of_func():
        start = time.time()
        func()
        end = time.time()
        print('Time : {} second.'.format(end - start))

    return time_of_func

@my_decorator
def my_log():
    import math
    a = math.log(144)
    print(f'log(144) = {a}')

my_log()
