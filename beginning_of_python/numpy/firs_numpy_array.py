import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

np_baseball = np.array(baseball)

print(type(np_baseball))

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2

print(bmi)
print(bmi[2:3])
print(bmi[:3])
print(bmi > 21.5)
print(bmi[bmi > 21.5])

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                  [65.4, 59.2, 63.6, 88.4, 68.7]])

print(np_2d.shape)
print(np_2d[1, 1])
# All rows but only second and third column
print(np_2d[:, 1:3])
# Only second row
print(np_2d[1, :])
