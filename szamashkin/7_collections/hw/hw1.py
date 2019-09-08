ingr = {"vegetables": ["mushrooms", "tomato"],
        "meat_types": ["poultry", "pork"],
        "cheese": ["brie", "parmesan"]}
predef1 = "pizza with " + ingr["vegetables"][0] + ", " + ingr["meat_types"][0] + ", " + ingr["cheese"][0]
predef2 = "pizza with " + ingr["vegetables"][1] + ", " + ingr["meat_types"][1] + ", " + ingr["cheese"][1]
#print(predef1), print(predef2)

order = input("If you want custom pizza, enter c, \nif predefined, enter p")
if order == "p":
    print("we have now:" + " " + predef1 + "\n" + predef2)
    order1 = input("If you want 1st pizza, enter 1, 2nd pizza, enter 2")
    if order1 == "1":
        print(predef1)
    elif order1 == "2":
        print(predef2)
if order == "c":
    print(f"you can use such ingredients:  {ingr}")
    your_order = input("Choose your ingredients: ")
    print(f"you ordered: {your_order}")
print("Thanks for your order, we will deliver in 60 minutes or the pizza will be free")