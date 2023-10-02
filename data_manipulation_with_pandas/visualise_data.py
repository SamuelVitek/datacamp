import pandas as pd
import matplotlib.pyplot as plt

avocados = pd.read_pickle('../data/avoplotto.pkl', nrows=6)
fff = pd.read_h

print(avocados.head())
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()
nb_sold_by_size.plot(kind='bar')
plt.show()

nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()
nb_sold_by_date.plot(x='date', y='', kind='line', rot=45)
plt.show()

avocados.plot(x='nb_sold', y='avg_price', kind='scatter', title='Number of avocados sold vs. average price')
plt.show()

avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins=20)
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5, bins=20)
plt.legend(["conventional", "organic"])
plt.show()

print(avocados.isna())
print(avocados.isna().any())
avocados.isna().sum().plot(kind='bar')
plt.show()

avocados_complete = avocados.dropna()
print(avocados_complete.isna().any())

avocados_list = [
    {'date': '2019-11-03', 'small_sold': 10376832, 'large_sold': 7835071},
    {'date': '2019-11-10', 'small_sold': 10717154, 'large_sold': 8561348},
]
avocados_2019 = pd.DataFrame(avocados_list)
print(avocados_2019)

avocados_dict = {
  "date": ['2019-11-17', '2019-12-01'],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}
avocados_2019 = pd.DataFrame(avocados_dict)
print(avocados_2019)
