import pandas as pd

temperatures = pd.read_csv('../data/temperatures.csv')

print(temperatures)
temperatures_ind = temperatures.set_index('city')
print(temperatures_ind)
print(temperatures_ind.reset_index())
print(temperatures_ind.reset_index(drop=True))

cities = ["Moscow", "Saint Petersburg"]
print(temperatures[temperatures['city'].isin(cities)])
print(temperatures_ind.loc[cities])

temperatures_ind = temperatures.set_index(['country', 'city'])
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]
print(temperatures_ind.loc[rows_to_keep])

print(temperatures_ind.sort_index())
print(temperatures_ind.sort_index(level=["city"]))
print(temperatures_ind.sort_index(level=["country", "city"], ascending=[True, False]))

temperatures_srt = temperatures_ind.sort_index()
print(temperatures_srt.loc['Pakistan':'Russia'])
# EMPTY
print(temperatures_srt.loc['Lahore': 'Moscow'])
print(temperatures_srt.loc[('Pakistan', 'Lahore'):('Russia', 'Moscow')])

print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])
print(temperatures_srt.loc[:, 'date':'avg_temp_c'])
print(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad'), 'date':'avg_temp_c'])

temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)
temperatures_ind = temperatures.set_index('date').sort_index()
print(temperatures_ind.loc['2010':'2011'])
print(temperatures_ind.loc['2010-08':'2011-02'])

print(temperatures.iloc[22, 1])
print(temperatures.iloc[:5])
print(temperatures.iloc[:, 2:4])
print(temperatures.iloc[:5, 2:4])

# temperatures['year'] = temperatures['date'].dt.year
print(temperatures)
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country', 'city'], columns='date')
print(temp_by_country_city_vs_year)

print(temp_by_country_city_vs_year.loc['Egypt':'India'])
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India','Delhi')])
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India','Delhi'), '2005':'2010'])

mean_temp_by_year = temp_by_country_city_vs_year.mean()
print(mean_temp_by_year[mean_temp_by_year == mean_temp_by_year.max()])
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis='columns')
print(mean_temp_by_city[mean_temp_by_city == mean_temp_by_city.min()])

