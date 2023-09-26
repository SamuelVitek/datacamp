# NumPy recap
import numpy as np

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
print('Bmi\n', bmi)

print('\nBmi bigger than 23 (boolean)\n', bmi > 23)
print('\nBmi bigger than 23 (actual values)\n', bmi[bmi > 23])

# Filtering Pandas DataFrames
import pandas as pd

brics = pd.read_csv('../data/brics.csv', index_col=0)
print('\nPrint BRICS\n', brics)

is_huge = brics['area'] > 8
print('\nPrint where area is greater than 8mil km\n', brics[is_huge])

print('\nCountries with population between 100mil and 300mil (using NumPy as a one line statement)\n',
      brics[np.logical_and(brics['population'] > 100, brics['population'] < 300)])
