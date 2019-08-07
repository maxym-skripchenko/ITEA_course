for i in range(51):

    if not i % 3 and not i % 5 and i!=0:

        print('FizzBuzz')

    elif i==0:
        print(i)
        continue

    elif not i % 3:

        print('Fizz')

    elif not i % 5:

        print('Buzz')

    else:

        print(i)