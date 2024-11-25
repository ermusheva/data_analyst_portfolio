# Delete all total values from csv-file, because they do not fit the real sums

# Divide raw csv data to 2 csv-files: export (in tonnes and euros) and import (in tonnes and euros)

import pandas as pd

# Load row csv file
df = pd.read_csv('data//aggregate_trash.csv')

# Display the first few rows to verify
print("Original data:")
print(df.head())

# Convert 'stk_flow' and 'unit' columns to uppercase to ensure consistency
df['stk_flow'] = df['stk_flow'].str.upper()
df['unit'] = df['unit'].str.upper()

# Define the list of flow types and units
flows = ['EXP', 'IMP']
units = ['T', 'THS_EUR']

# Check for incorrect values
print("\nNumber of incorrect values in 'stk_flow' :")
print((~df['stk_flow'].isin(flows)).sum())

print("\nNumber of incorrect values in 'units' :")
print((~df['unit'].isin(units)).sum())

# Filter all not-total values
filter_rows = (df['rawmat'] != 'TOTAL') & (df['geo'] != 'EU27_2020') & (~df['partner'].isin(['EXT_EU27_2020', 'INT_EU27_2020']));
filter_df = df[filter_rows]


# Separate the data into export and import
export_df = filter_df[filter_df['stk_flow'] == 'EXP']
import_df = filter_df[filter_df['stk_flow'] == 'IMP']

# Transform the export data
export_trans = export_df.pivot_table(
    index=['rawmat', 'partner', 'geo', 'TIME_PERIOD'],
    columns='unit',
    values='OBS_VALUE',
    aggfunc='sum'
).reset_index()
# Transform the import data
import_trans = import_df.pivot_table(
    index=['rawmat', 'partner', 'geo', 'TIME_PERIOD'],
    columns='unit',
    values='OBS_VALUE',
    aggfunc='sum'
).reset_index()


# Save the divided data to new CSV files
export_trans.to_csv('data//export_trash.csv', index=False)
import_trans.to_csv('data//import_trash.csv', index=False)


# Print the transformed DataFrames
print("\nExport data:")
print(export_trans.head())
print("\nImport data:")
print(import_trans.head())



'''
# Define the output file names for divided data
output_files = {
    ('EXP', 'T'): 'data//export_tonnes.csv',
    ('EXP', 'THS_EUR'): 'data//export_euros.csv',
    ('IMP', 'T'): 'data//import_tonnes.csv',
    ('IMP', 'THS_EUR'): 'data//import_euros.csv'
}

for flow in flows:
    for unit in units:
        condition = (df['stk_flow'] == flow) & (df['unit'] == unit)
        filtered_df = df[condition]
        output_file = output_files[(flow, unit)]
        filtered_df.to_csv(output_file, index=False)
        print(f"Saved {output_file} with {len(filtered_df)} records.")
'''
