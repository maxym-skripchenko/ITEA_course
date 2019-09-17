rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")

print("\nThe following rivers are in dic:")
for river in rivers.keys():
    print("- " + river.title())

print("\nThe following countries are in dic:")
for country in rivers.values():
    print("- " + country.title())