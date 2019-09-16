pizzas = ['hawai', 'four cheese', 'pepperoni']

friend_pizzas = pizzas[:]
print(friend_pizzas)
print("\n")

pizzas.append('diabolo')
print("My favorite pizzas are: ")

for pizza in pizzas[:]:
    print(pizza.title())

print("\n")
friend_pizzas.append('vegetarian')
print("My friend’s favorite pizzas are:")

for friend_pizza in friend_pizzas[:]:
    print(friend_pizza.title())

