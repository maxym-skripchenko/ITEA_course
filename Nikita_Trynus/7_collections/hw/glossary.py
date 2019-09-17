words = ['Cucumber', 'Tomatoes', 'Cheese']
meanings = ['green vegetable', 'red vegetable', 'yellow not vegetable']
glossary = dict(zip(words, meanings))
if __name__ == '__main__':

    for word, meaning in glossary.items():
        print(f'{word}: {meaning}\n')

    """
    
    ANIMALS
    
    """

    fred = {'kind': 'german shepard', 'owner': 'Nikita'}
    barsik = {'kind': 'I do not now', 'owner': 'Maybe person'}

    animals = [fred, barsik]

    for pet in animals:
        print(pet)
