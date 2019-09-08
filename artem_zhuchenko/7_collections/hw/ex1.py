    # * Create 3-4 lists with pizza ingredients groups (vegetables, meat_types...).
    # * Create list with predefined pizzas.
    # * Ask user what pizza he want (custom or predefined).
    # * Output variants of pizza or ingredient step by step
    # * Return result of ordered pizza

list_of_ingredients_vegetables = ["tomatoes", "olives", "corn", "pepper",
                                  "cucumber", "mushrooms", "onion"]
list_of_ingredients_meat = ["chicken", "sausages", "bacon", "turkey",
                            "pepperoni", "veal", "ham", "salmon"]
list_of_ingredients_fruits = ["pineapple"]
list_of_ingredients_cheese = ["mozarella", "bergader blue", "parmesan",
                              "cheddar", "feta", "philadelphia"]
list_of_ingredients_sauces = ["bbq", "alfredo's", "garlic", "domino's"]

list_os_lists_of_ingredients = [list_of_ingredients_vegetables, list_of_ingredients_meat,
                                list_of_ingredients_fruits,
                                list_of_ingredients_cheese, list_of_ingredients_sauces]

pizza_tony_pepperoni = [list_of_ingredients_meat[4],
                        list_of_ingredients_cheese[0:2], list_of_ingredients_sauces[1]]
pizza_texas = [list_of_ingredients_vegetables[2], list_of_ingredients_vegetables[6],
               list_of_ingredients_meat[1]]
pizza_margherita = [list_of_ingredients_cheese[0],
                    list_of_ingredients_cheese[2], list_of_ingredients_sauces[3]]

predefined_pizzas = [pizza_tony_pepperoni, pizza_texas, pizza_margherita]


def user_ingredient_selection(ingredient_number, ingedients_category):
    ingredient_number = int(ingredient_number)
    ingredient_number -= 1
    return ingedients_category[ingredient_number]

def user_selection():
    while True:
        user_option_selection = input("What pizza do you want?\
        (Type 1 for Predefined Pizza, 2 for Custom Pizza!): ")
        try:
            assert user_option_selection == "1" or user_option_selection == "2"
        except AssertionError:
            print("Please use 1 or 2 to select your option! ")
        else:
            user_option_selection = int(user_option_selection)
            break

    if user_option_selection == 1:
        print(predefined_pizzas)
        while True:
            selected_predefined_pizza = input("Select your pizza: 1 - Tony Pepperoni,\
            2 - Texas, 3 - Margherita:")
            try:
                selected_predefined_pizza = int(selected_predefined_pizza)
            except ValueError:
                print("Please select one of the options!")
            else:
                try:
                    assert len(predefined_pizzas) >= selected_predefined_pizza > 0
                except AssertionError:
                    print(f"Sorry, we have only {len(predefined_pizzas)} pizzas at the moment :(")
                else:
                    break

        selected_predefined_pizza -= 1

        print(f"In your pizza: {predefined_pizzas[selected_predefined_pizza]}")
    else:
        print("Welcome to constructor! Please select ingredient from the list below")

        for ingedients_category in list_os_lists_of_ingredients:
            print(ingedients_category)
            while True:
                ingredient_number = input("Please type ingredient number: ")
                try:
                    ingredient_number = int(ingredient_number)
                except ValueError:
                    print("Please select number of ingredient from the list!")
                else:
                    try:
                        assert len(ingedients_category) >= ingredient_number < 0
                    except AssertionError:
                        print("There are not so many ingredients in list!")
                    else:
                        break


        print(f"You've added " f"{user_ingredient_selection(ingredient_number=ingredient_number,ingedients_category=ingedients_category)}!")


user_selection()
