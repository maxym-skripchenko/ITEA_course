vegetables = ['cucumber', 'tomatoes', 'carrot']*2
meat = ['beef', 'pork', 'chicken']*2
cheese = ['one', 'two', 'three']*2

pizza = ['1','2','3']


if __name__ == '__main__':

    choice = input('Which pizza do you prefer: ')
    for veg in vegetables:
        print(veg)

    print(sorted(pizza))

    friend_pizzas = pizza[:]
    pizza.append('paperoni')
    friend_pizzas.append('different pizza')
    print(friend_pizzas==pizza)

    print('My fav pizzas: ')
    for piz in pizza:
        print(piz)
    print('My frien fav pizzas: ')
    for piz in pizza:
        print(piz)
