import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

food_consumption = pd.read_csv('../data/food_consumption.csv', index_col=0)

print(food_consumption.head())

food_consumption_belgium = food_consumption[food_consumption['country'].isin(['Belgium'])]
food_consumption_usa = food_consumption[food_consumption['country'].isin(['USA'])]
print(food_consumption_belgium)

# Calculate mean and median consumption in Belgium
print('Consumption in Belgium - Average', food_consumption_belgium['consumption'].mean())
print('Consumption in Belgium - Average', food_consumption_belgium['consumption'].median())

# Calculate mean and median consumption in USA
print('Consumption in USA - Average', food_consumption_usa['consumption'].mean())
print('Consumption in USA - Average', food_consumption_usa['consumption'].median())

belgium_and_usa = food_consumption[food_consumption['country'].isin(['Belgium', 'USA'])]
print(belgium_and_usa)

belgium_and_usa_grouped = belgium_and_usa.groupby('country')['consumption'].agg(['mean', 'median'])
print(belgium_and_usa_grouped)
belgium_and_usa_grouped.plot(kind='bar', rot=0)
plt.legend(['Average', 'Median'])
plt.show()

rice_consumption = food_consumption[food_consumption['food_category'].isin(['rice'])]
rice_consumption['co2_emission'].hist()
plt.show()

print(belgium_and_usa.groupby('country')['consumption'].agg(['mean', 'median']))

print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))
print(np.quantile(food_consumption['co2_emission'], [0, 0.2, 0.4, 0.6, 0.8, 1]))
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))


print(food_consumption.groupby('food_category')['co2_emission'].agg(['var', 'std']))
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
plt.show()

food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist()
plt.show()

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()
print(emissions_by_country)
q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = emissions_by_country[(emissions_by_country < lower) | (emissions_by_country > upper)]
print(outliers)
