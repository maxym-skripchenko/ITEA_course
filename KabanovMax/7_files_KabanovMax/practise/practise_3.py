menu = ('Vodka', 'Bourbon', 'Tequila', 'Whisky', 'Rom')


print("You can choose from the following menu items:")
for item in menu:
    print("- " + item)

menu_items = ('Vodka', 'Bourbon', 'Beer', 'Schnapps', 'Rom')
print("\nOur menu has been updated.")

print("\nYou can now choose from the following items:")
for item in menu_items:
    print("- " + item)

print("\nLast two items are:")
print(menu_items[2:4])

print("\nEvery second item are:")
print(menu_items[1::2])

print("\nReversed order are:")
print(menu_items[::-1])