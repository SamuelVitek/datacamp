import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop)
# Logarithmic scale
plt.xscale('log')
plt.show()
plt.clf()

plt.scatter(year, pop)
plt.show()
plt.clf()

print(year[len(year) - 1])

# help(plt.hist)

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.show()
plt.clf()

year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6],
           ['0', '2B', '4B', '6B'])
plt.show()
plt.clf()

gap = pd.read_csv('../data/cca_gapminder.csv')

pop2 = np.array([gap['population'].values])
np_pop = (pop2 / 1000000) * 2

continents = np.array(gap['cont'].values)
color_dict = {
    'Asia': 'red',
    'Europe': 'green',
    'Africa': 'blue',
    'Americas': 'yellow',
    'Oceania': 'black'
}
colors = [color_dict[continent] for continent in continents]

plt.scatter(gap['gdp_cap'].values, gap['life_exp'].values, s=np_pop, c=colors, alpha=0.8)
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

plt.xticks(tick_val, tick_lab)

plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

plt.grid(True)

plt.show()
