import numpy as np
import pandas as pd

# While loop
offset = -6

while offset != 0:
    print('correcting...')
    if offset > 0:
        offset -= 1
    else:
        offset += 1
    print(offset)

# For loop
fam = [1.73, 1.68, 1.71, 1.89]
print('\nFamily list\n', fam, '\n')

for member in fam:
    print(member)

print('\nUsing enumerate')
for index, height in enumerate(fam):
    print('Index ' + str(index) + ': ' + str(height))

print('\nManipulating string using for-loop')
for letter in 'family':
    print(letter.capitalize())

print('\nFor-loop practice')
house = [['hallway', 11.25],
         ['kitchen', 18.0],
         ['living room', 20.0],
         ['bedroom', 10.75],
         ['bathroom', 9.50]]

for rooms in house:
    print('the ' + str(rooms[0]) + ' is ' + str(rooms[1]) + ' sqm')

# Looping through data structures
print('\nLooping through data structures')
world = {'afghanistan': 30.55,
         'albania': 2.77,
         'algeria': 39.21}

for country, population in world.items():
    print(country + '--' + str(population))

print('\nLooping through NumPy array')
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2

for val in bmi:
    print(val)

print('\nLooping through NumPy array with nditer')
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
mean = np.array([np_height, np_weight])

for val in np.nditer(mean):
    print(val)

# Looping through DataFrames
brics = pd.read_csv('../data/brics.csv', index_col=0)

print('\nLoops through the column names')
for col_name in brics:
    print(col_name)

print('\nIterating through the DataFrame')
for label, row in brics.iterrows():
    print(label)
    print(row, '\n')

print('\nPrint only label and capital for each observation (row)')
for lab, row in brics.iterrows():
    print(lab + ': ' + row['capital'])

print('\nAdding new column with number of letters in country\'s name')
for lab, row in brics.iterrows():
    brics.loc[lab, 'coun_name_length'] = len(row['country'])

print(brics)

print('\nMore efficient way to add a calculated column (without a for-loop)')
brics['country_name_length'] = brics['country'].apply(len)

print(brics)
