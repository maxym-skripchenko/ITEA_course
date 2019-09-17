ingrid_group = {'vegetables': ['pepper', 'tomato'],
                'meat_types': ['bacon', 'chicken', 'ham'],
                'cheese': ['brie', 'blue', 'gouda']}

pizza_bacon = ingrid_group['vegetables'][0] + ' ' + ingrid_group['meat_types'][0] + ' ' + ingrid_group['cheese'][0]
#print(f'This is pizza_bacon, ingredients: {pizza_bacon}')

pizza_chicken = ingrid_group['vegetables'][1] + ' ' + ingrid_group['meat_types'][1] + ' ' + ingrid_group['cheese'][1]
#print(f'This is pizza_chicken, ingredients: {pizza_chicken}')

pizza_ham = ingrid_group['vegetables'][1] + ' ' + ingrid_group['meat_types'][2] + ' ' + ingrid_group ['cheese'][2]
#print(f'This is pizza_ham, ingredients: {pizza_ham}')

ordered_pizza = input('What pizza you wants ? If custom - enter - c, for predefined - enter - p  -->')
if ordered_pizza == 'p':
    print(f'Pizza_bacon, ingredients: {pizza_bacon}')
    print(f'Pizza_chicken, ingredients: {pizza_chicken}')
    print(f'Pizza_ham, ingredients: {pizza_ham}')
    choice = input('Made choice, pizza_bacon - enter - b, pizza_chicken - enter - ch, pizza_ham - enter h : ')
    if choice == 'b':
        print(f'Your favorite pizza - pizza_bacon, ingredients: {pizza_bacon}')
    elif choice == 'ch':
        print(f'Your favorite pizza - pizza_chicken, ingredients: {pizza_chicken}')
    elif choice == 'h':
        print(f'Your favorite pizza - pizza_ham, ingredients: {pizza_ham}')
    pass
if ordered_pizza == 'c':
    your_pizza = input('Enter your ingredients: ')
    print(f'This is your_pizza, ingredients: {your_pizza}')

#print(f'Your favorite ordered pizza: {ordered_pizza}')