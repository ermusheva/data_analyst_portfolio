import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load result csv file
total_eu_export_import = pd.read_csv('..//results//eu_export_import_by_years.csv')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))


# width of the bars
barWidth = 0.3 

export_bars = total_eu_export_import['export_thousand_euros']
import_bars = total_eu_export_import['import_thousand_euros']

# Define a colormap
cmap = plt.get_cmap("plasma", 2)

# The x position of bars
r1 = np.arange(len(export_bars))
r2 = [x + barWidth for x in r1]
years = total_eu_export_import['time_period']
 
# Create bars
ax.bar(r1, export_bars, width = barWidth, color = cmap(0), edgecolor = 'black', capsize=7, label='export')
ax.bar(r2, import_bars, width = barWidth, color = cmap(1), edgecolor = 'black', capsize=7, label='import')
 
# general layout
plt.xticks([r + barWidth for r in range(1, len(export_bars), 2)], years[1:len(years):2])
ax.set_ylabel("Billions \N{euro sign}")
ax.set_title('Total export and import of the European Union by years, \N{euro sign}')
ax.legend()

# Format the y-axis to show values in billions
def to_billions(y, pos):
    return f'{y / 1e6:.1f}B'

ax.yaxis.set_major_formatter(FuncFormatter(to_billions))
 
plt.tight_layout()
plt.savefig('..//assets//eu_export_import_by_years.png', dpi=300)
plt.show()

