import matplotlib.pyplot as plt
from scipy.stats import uniform, binom
import pandas as pd
import numpy as np

amir_deals = pd.read_csv('../data/amir_deals.csv', index_col=0)

print(amir_deals.head())

counts = amir_deals['product'].value_counts()
print(counts)

probs = counts / counts.sum()
print(probs * 100)

np.random.seed(24)

sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

sample_without_replacement = amir_deals.sample(5, replace=True)
print(sample_without_replacement)


min_time = 0
max_time = 30

# Calculate probability of waiting less than 5 mins
prob_less_than_5 = uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)

# Calculate probability of waiting more than 5 mins
prob_greater_than_5 = uniform.cdf(max_time, 5, max_time)
print(prob_greater_than_5)

# Calculate probability of waiting 10-20 mins
prob_between_10_and_20 = uniform.cdf(20, 10, 30)
print(prob_between_10_and_20)

np.random.seed(334)
wait_times = uniform.rvs(0, 30, size=1000)
print(wait_times)

plt.hist(wait_times)
plt.show()

np.random.seed(10)
# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))
# Simulate 1 week of 3 deals
print(binom.rvs(3, 0.3, size=1))
# Simulate 52 weeks of 3 deals
deals = binom.rvs(3, 0.3, size=52)
print(len(deals), deals.sum(), deals.mean())

# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)
# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)
# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)
print(prob_3, prob_less_than_or_equal_1, prob_greater_than_1)

# Expected number won out of 3 with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)
# Expected number won out of 3 with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)
# Expected number won out of 3 with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)

