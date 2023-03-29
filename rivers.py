rivers = {'nile' : 'egypt',
          'amazon': 'brazil',
          'drina': 'serbia',
          'volga': 'russia'}
for river,country in rivers.items():
    print(f"The {river.title()} through {country.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())