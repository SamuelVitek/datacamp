from scipy.stats import norm, poisson, expon
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

world_happiness = pd.read_csv('../data/world_happiness.csv')

sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)
plt.show()
sns.lmplot(x="life_exp", y="happiness_score", data=world_happiness, ci=None)
plt.show()

cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])
print(cor)

sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)
plt.show()
cor_before_log = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])


world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()

cor_after_log = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor_before_log, cor_after_log)