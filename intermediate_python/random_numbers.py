import numpy as np
import matplotlib.pyplot as plt

# Pseudo random number
np.random.seed(123)
print(np.random.rand())
print(np.random.rand())

# Repeatability using seed
np.random.seed(123)
print('\n', np.random.rand())
print(np.random.rand())

# Coin toss (randomly either 0 or 1)
np.random.seed(123)
coin = np.random.randint(0, 2)

print('\n', coin)

if coin == 0:
    print('heads')
else:
    print('tails')

print('\n10 coin tosses')
outcomes = []
for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')

print(outcomes)

print('\nRandom walk for 10 coin tosses')
tails = [0]
for x in range(10):
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)

print(tails)

np.random.seed(123)
total_tails = []
for x in range(10000):
    tails = [0]
    for y in range(10):
        coin = np.random.randint(0, 2)
        tails.append(tails[y] + coin)
    total_tails.append(tails[-1])

help(plt.hist)
print(total_tails)

bins = [n for n in range(11)]

plt.hist(total_tails, bins, edgecolor='black', align='left')
plt.xticks(bins)
plt.show()
