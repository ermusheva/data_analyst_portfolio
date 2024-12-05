# Delete all trade values of materials and partners subcategories

# Divide raw csv data to 2 csv-files: export (in tonnes and euros) and import (in tonnes and euros)

import pandas as pd

# Load row csv file
waste = pd.read_csv('..//data//aggregate_trash.csv')
materials = pd.read_csv('..//data//material_labels.csv')

# Display the first few rows of waste data to verify
print("Original waste data:")
print(waste.head())

# Convert 'stk_flow' and 'unit' columns to uppercase to ensure consistency
waste['stk_flow'] = waste['stk_flow'].str.upper()
waste['unit'] = waste['unit'].str.upper()

# Define the list of flow types and units
flows = ['EXP', 'IMP']
units = ['T', 'THS_EUR']

# Check for incorrect values
print("\nNumber of incorrect values in 'stk_flow' :")
print((~waste['stk_flow'].isin(flows)).sum())

print("\nNumber of incorrect values in 'units' :")
print((~waste['unit'].isin(units)).sum())

# Delete all trades subcategory materials
subcat_materials_rows = materials['Codes'].str.contains('_')
filter_materials = materials[~subcat_materials_rows]
# Delete 'Hong Kong' from partners as a part of 'China including Hong Kong' partner
filter_rows = waste['rawmat'].isin(filter_materials['Codes']) & (waste['partner'] != 'HK');
filter_waste = waste[filter_rows]


# Separate the data into export and import
export_waste = filter_waste[filter_waste['stk_flow'] == 'EXP']
import_waste = filter_waste[filter_waste['stk_flow'] == 'IMP']

# Transform the export data
export_trans = export_waste.pivot_table(
    index=['rawmat', 'partner', 'geo', 'TIME_PERIOD'],
    columns='unit',
    values='OBS_VALUE',
    aggfunc='sum'
).reset_index()
# Transform the import data
import_trans = import_waste.pivot_table(
    index=['rawmat', 'partner', 'geo', 'TIME_PERIOD'],
    columns='unit',
    values='OBS_VALUE',
    aggfunc='sum'
).reset_index()


# Save the divided data to new CSV files
export_trans.to_csv('..//data//export_trash.csv', index=False)
import_trans.to_csv('..//data//import_trash.csv', index=False)


# Print the transformed DataFrames
print("\nExport waste data:")
print(export_trans.head())
print("\nImport waste data:")
print(import_trans.head())
