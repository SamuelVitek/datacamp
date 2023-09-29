import pandas as pd

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', None)

homelessness = pd.read_csv('../data/homelessness.csv', index_col=0)

print('\n')
print(homelessness.head())

print('\n')
print(homelessness.info())

print('\n')
print(homelessness.shape)

print('\n')
print(homelessness.describe())

print('\n')
print(homelessness.values)

print('\n')
print(homelessness.columns)

print('\n')
print(homelessness.index)

print('\n')
print(homelessness.sort_values('state_pop'))
print(homelessness.sort_values('state_pop', ascending=False))

print('\n')
homelessness_reg_fam = homelessness.sort_values(['region', 'family_members'], ascending=[True, False])
print(homelessness_reg_fam.head())

print('\n')
columns_to_subset = ['region', 'state', 'state_pop']
print(homelessness[columns_to_subset])

print('\n')
print(homelessness[['region', 'state', 'state_pop']])

is_enc = homelessness['region'] == 'East North Central'
small = homelessness['state_pop'] > 1000000
df = homelessness[homelessness['state'].str.startswith('M')]
print(homelessness[is_enc & small])

isin = homelessness['state'].isin(['Texas', 'California', 'Wisconsin'])
print(homelessness[isin])

family_members = homelessness['family_members'] < 1000
region = homelessness['region'] == 'Pacific'

together = homelessness[(homelessness['family_members'] < 1000) & (homelessness['region'] == 'Pacific')]
print(together)

homelessness['total'] = homelessness['individuals'] + homelessness['family_members']
homelessness['p_individuals'] = homelessness['individuals'] / homelessness['total']
print(homelessness)

homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']
print(homelessness.head())


homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']
high_homelessness = homelessness[homelessness['indiv_per_10k'] > 20]
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k', ascending=False)
result = high_homelessness_srt[['state', 'indiv_per_10k']]
print(result)
