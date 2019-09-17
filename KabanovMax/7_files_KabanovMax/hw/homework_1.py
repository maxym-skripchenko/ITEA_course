pizza_parts = {
    "vegetables": ["corn", "cucumber", "tomato"],
    "meat": ["chicken", "pork", "beef"],
    "cheese": ["brie", "parmesan"]
        }

def_pizza_1 = "Pizza #1 with " + pizza_parts["vegetables"][0] + ", " + pizza_parts["meat"][0] + ", " + pizza_parts["cheese"][0]
def_pizza_2 = "Pizza #2 with " + pizza_parts["vegetables"][2] + ", " + pizza_parts["meat"][1] + ", " + pizza_parts["cheese"][1]


order = input("You want pizza from menu? Enter 'Yes' or 'No': ")
if order == "Yes":
    print("In menu now:" + "\n" + def_pizza_1 + "\n" + def_pizza_2)
    order_menu = input("Enter number of desired pizza: ")
    if order_menu == "1":
        print("Thank you for your order, your pizza # 1. Wait for delivery")
    elif order_menu == "2":
        print("Thank you for your order, your pizza # 2. Wait for delivery")

if order == "No":
    print(f"You can use such ingredients: {pizza_parts}")
    your_order = input("Choose your ingredients: ")
    print(f"You ordered is: {your_order}. Good choice, wait for delivery")

