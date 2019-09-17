pizza_ingredients = {"vegetables": ["tomato", "olives"],
                    "meat": ["pork", "chicken"],
                    "cheese": ["mozzarella", "parmesan"]
                    }
pork_pizza = pizza_ingredients["vegetables"][0] + ' ' + pizza_ingredients["meat"][0] + ' ' + pizza_ingredients["cheese"][0]
print(pork_pizza)
chicken_pizza = pizza_ingredients["vegetables"][1] + ' ' + pizza_ingredients["meat"][1] + ' ' + pizza_ingredients["cheese"][1]
print(chicken_pizza)
order = input("Choose pizza: ready-made or your own. Print : ready or own ")
if order == "ready":
    print(f"Pork pizza: {pork_pizza}")
    print(f"Chicken pizza: {chicken_pizza}")
    user_order = input("What do you like : Pork or Chicken pizza")
    if user_order == "Pork":
        print(f"You choose Pork pizza: {pork_pizza}")
    elif user_order == "Chicken":
        print(f"You choose Chicken pizza: {chicken_pizza}")
if order == "own":
    print(f"We have : {pizza_ingredients}")
    user_choice = input("Enter your ingredients: ")
    print(f"You choose: {user_choice}")
