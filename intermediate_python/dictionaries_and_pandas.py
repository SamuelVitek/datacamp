import pandas as pd

pop = [30.55, 2.77, 39.21]
countries = ['Afghanistan', 'Albania', 'Algeria']

index = countries.index('Albania')
print(pop[index])

world = {'Afghanistan': 30.55, 'Albania': 2.77, 'Algeria': 39.21}
print(world['Albania'])
print(world.keys())

world['sealand'] = 0.000027
print(world)
print('sealand' in world)

world['sealand'] = 0.000028
print(world['sealand'])

del (world['sealand'])
print(world)

dicti = {'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
         'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
         'area': [8.516, 17.10, 3.286, 9.597, 1.221],
         'population': [200.4, 143.5, 1252, 1357, 52.98]}

index_variables = ['BR', 'RU', 'IN', 'CH', 'SA']

brics = pd.DataFrame(dicti)
print('\nDictionary\n', dicti)
print('\nFrom dictionary\n', brics)

brics.index = index_variables
print('\nAdded index\n', brics)

brics = pd.read_csv('../data/brics.csv', index_col=0)
print('\nUsing .read_csv\n', brics)
print('\nSelect countries with brackets (Pandas object called Series)\n', brics['country'])
print('\nSelect countries with brackets (DataFrame)\n', brics[['country']])
print('\nSelect countries and capitals with brackets\n', brics[['country', 'capital']])

print('\nSelect only second to fourth row\n', brics[1:4])

print('\nUsing loc\n', brics.loc[['RU', 'IN'], ['country', 'capital']])
print('\nUsing loc (all rows specific columns)\n', brics.loc[:, ['country', 'capital']])

print('\nUsing iloc\n', brics.iloc[[0, 4], [0, 1]])
print('\nUsing iloc\n', brics.iloc[:, [0, 1]])
