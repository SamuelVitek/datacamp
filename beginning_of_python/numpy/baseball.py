import numpy as np
import pandas as pd

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

np_baseball = np.array(baseball)

print(type(np_baseball))
print(np_baseball.shape)

mbl = pd.read_csv('../../data/baseball.csv')

np_baseball = np.array([mbl["Height"].values, mbl["Weight"].values])
np_pos_category = np.array(mbl["PosCategory"].values)
catchers = np.array(np_baseball[:, np_pos_category == 'Catcher'])
print(np_baseball)
print(catchers)

print(np.mean(np_baseball[1, :]))

# Sort all from smallest to highest and choose the middle one
print(np.median(np_baseball[1, :]))

# Correlation between height and weight and standard deviation
print(np.corrcoef(np_baseball[0, :], np_baseball[1, :]))
print(np.std(np_baseball[1, :]))
