import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import font_manager

# Load result csv file
total_eu_export_import = pd.read_csv('..//results//eu_export_import_by_years.csv')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(16, 9), constrained_layout=True)

export_data = total_eu_export_import['export_thousand_euros']
import_data = total_eu_export_import['import_thousand_euros']

# Define a colormap
cmap = plt.get_cmap("plasma", 2)

years = total_eu_export_import['time_period']


ax.plot(years, export_data, color = cmap(0), label='export')
ax.plot(years, import_data, color = cmap(1), label='import')
 
# general layout
font_props = font_manager.FontProperties(family='sans-serif', size=14)
ax.set_xticks(years[1:len(years):2])
ax.set_xticklabels(years[1:len(years):2], fontproperties=font_props)

fig.suptitle('Total export and import of the European Union by years, Billions \N{euro sign}', fontsize=16, fontweight="bold", fontfamily='sans-serif')
ax.legend(loc='upper left', prop=font_props)

# Format the y-axis to show values in billions
def to_billions(y, pos):
    return f'{y / 1e6:.1f}B'

ax.yaxis.set_major_formatter(FuncFormatter(to_billions))
ax.set_yticks(ax.get_yticks())
ax.set_yticklabels([to_billions(tick, None) for tick in ax.get_yticks()], fontproperties=font_props)
 
# plt.tight_layout()
plt.savefig('..//assets//eu_export_import_by_years.png', dpi=300)
plt.show()

