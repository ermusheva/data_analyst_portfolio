import pandas as pd

# Load result csv file
eu_partners_by_year = pd.read_csv('..//results//top_10_export_partners_by_years.csv')
eu_partners = eu_partners_by_year.pivot_table(
    index=['partner_label'],
    columns='time_period',
    values='thousand_euros',
    aggfunc='sum'
).reset_index()

# Replace country names to shorter names
eu_partners.loc[:, 'partner_label'] = eu_partners['partner_label'].replace('United Kingdom', 'UK');
eu_partners.loc[:, 'partner_label'] = eu_partners['partner_label'].replace('United States', 'USA');
eu_partners.loc[:, 'partner_label'] = eu_partners['partner_label'].replace('China including Hong Kong', 'China');
eu_partners.loc[:, 'partner_label'] = eu_partners['partner_label'].replace('Turkiye', 'Turkey');
print(eu_partners.head())

# Save the data to new CSV files
eu_partners.to_csv('..//results//eu_top_10_export_partners.csv', index=False)