import matplotlib.pyplot as plt
from scipy.stats import norm, poisson, expon
import pandas as pd
import numpy as np

amir_deals = pd.read_csv('../data/amir_deals.csv', index_col=0)

amir_deals['amount'].hist(bins=10)
plt.show()

prob_under_7500 = norm.cdf(7500, amir_deals['amount'].mean(), amir_deals['amount'].std())
prob_over_1000 = 1 - norm.cdf(1000, amir_deals['amount'].mean(), amir_deals['amount'].std())
prob_3000_to_7000 = (norm.cdf(7000, amir_deals['amount'].mean(), amir_deals['amount'].std())
                     - norm.cdf(3000, amir_deals['amount'].mean(), amir_deals['amount'].std()))
print(prob_under_7500, prob_over_1000, prob_3000_to_7000)

pct_25 = norm.ppf(0.25, 5000, 2000)
print(pct_25)

new_mean = amir_deals['amount'].mean() * 1.2
new_sd = amir_deals['amount'].std() * 1.3
new_sales = norm.rvs(new_mean, new_sd, size=36)

plt.hist(new_sales)
plt.show()

amir_deals['num_users'].hist()
plt.show()

np.random.seed(104)

sample_means = []
for i in range(100):
    samp_20 = amir_deals['num_users'].sample(20, replace=True)
    samp_20_mean = np.mean(samp_20)
    sample_means.append(samp_20_mean)

sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
plt.show()

prob_5 = poisson.pmf(5, 4)
prob_coworker = poisson.pmf(5, 5.5)
print(prob_5, prob_coworker)

prob_2_or_less = poisson.cdf(2, 4)
prob_over_10 = 1 - poisson.cdf(10, 4)
print(prob_2_or_less, prob_over_10)

print(expon.cdf(1, scale=2.5))
print(1 - expon.cdf(4, scale=2.5))
print(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5))