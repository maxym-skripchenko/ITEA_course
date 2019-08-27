pizzas = ['hawaian', 'four cheese', 'papa jones']
friend_pizzas = pizzas[:]
print(friend_pizzas)
pizzas.append('dominos')
print("My favorite pizzas are:")
for pizza in pizzas[:]:
    print(pizza.title())
friend_pizzas.append('pizza hut')
print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
    print(friend_pizza.title())