import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load result csv file
total_eu_export_import = pd.read_csv('..//results//eu_export_import_by_years.csv')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(16, 9))

export_data = total_eu_export_import['export_thousand_euros']
import_data = total_eu_export_import['import_thousand_euros']

# Define a colormap
cmap = plt.get_cmap("plasma", 2)

# The x position
years = total_eu_export_import['time_period']

ax.plot(years, export_data, color = cmap(0), label='export')
ax.plot(years, import_data, color = cmap(1), label='import')
 
# general layout
plt.xticks(years[1:len(years):2])
ax.set_title('Total export and import of the European Union by years, Billions \N{euro sign}')
ax.legend()

# Format the y-axis to show values in billions
def to_billions(y, pos):
    return f'{y / 1e6:.1f}B'

ax.yaxis.set_major_formatter(FuncFormatter(to_billions))
 
# plt.tight_layout()
plt.savefig('..//assets//eu_export_import_by_years.png', dpi=300)
plt.show()

