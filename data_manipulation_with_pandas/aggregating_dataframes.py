import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', None)
sales = pd.read_csv('../data/sales_subset.csv')

print(sales.head())
print(sales.info())
print('\n')
print(sales['weekly_sales'].mean())
print(sales['weekly_sales'].median())

print(sales['date'].max())
print(sales['date'].min())


def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)


print(sales['temperature_c'].agg(iqr))
print(sales[["temperature_c", 'fuel_price_usd_per_l', 'unemployment']].agg(iqr))
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr, np.median]))

sales_1_1 = sales.sort_values('date')
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
sales_1_1['cum_max_sales'] = sales_1_1['weekly_sales'].cummax()
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

store_types = sales.drop_duplicates(subset=['store', 'type'])
print(store_types.head())
store_depts = sales.drop_duplicates(subset=['store', 'department'])
print(store_depts.head())
holiday_dates = sales[sales['is_holiday'] == True].drop_duplicates('date')
print(holiday_dates['date'])

store_counts = store_types['type'].value_counts()
print(store_counts)
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)

sales_all = sales["weekly_sales"].sum()
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
sales_B = sales[sales['type'] == 'B']['weekly_sales'].sum()
sales_C = sales[sales['type'] == 'C']['weekly_sales'].sum()
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_propn_by_type = sales_by_type / sum(sales['weekly_sales'])
print(sales_propn_by_type)

sales_by_type = sales.groupby("type")["weekly_sales"].sum()
sales_by_type_is_holiday = sales.groupby(['type', 'is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min, np.max, np.mean, np.median])
print(sales_stats)
unemp_fuel_stats = sales.groupby('type')[['unemployment', 'fuel_price_usd_per_l']].agg(
    [np.min, np.max, np.mean, np.median])
print(unemp_fuel_stats)

mean_sales_by_type = sales.pivot_table(values='weekly_sales', index='type')
print(mean_sales_by_type)
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales', index='type', aggfunc=[np.mean, np.median])
print(mean_med_sales_by_type)
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales', index='type', columns='is_holiday')
print(mean_sales_by_type_holiday)

print(sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0))
print(sales.pivot_table(values='weekly_sales', index='department', columns='type', fill_value=0, margins=True))
