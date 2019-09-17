favorite_pizzas = ["Pork", "Chicken"]
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("Four cheeses")
friend_pizzas.append("Beef")

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print("- " + pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print("- " + pizza)