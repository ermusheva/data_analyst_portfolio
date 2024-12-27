import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Load result csv file
eu_export_by_materials = pd.read_csv('..//results//eu_export_by_years_materials.csv')

eu_export_2021 = eu_export_by_materials[eu_export_by_materials['time_period'] == 2021]
# Replace material names to shorter names
eu_export_2021.loc[:, 'material_label'] = eu_export_2021['material_label'].replace('Not specified', 'Not spec');
eu_export_2021.loc[:, 'material_label'] = eu_export_2021['material_label'].replace('Paper and cardboard', 'Paper');
print(eu_export_2021.head())
print(len(eu_export_2021))

# Define a colormap
cmap = plt.get_cmap("plasma", 2)

fig, ax = plt.subplots(figsize=(16, 9), constrained_layout=True)
bars = ax.barh(eu_export_2021['material_label'], eu_export_2021['tonne'], color = cmap(0), edgecolor = 'black', capsize=7, label=eu_export_2021['tonne'])

ax.set_title('Total export of the European Union in 2021 by materials, Millions tonnes')
ax.invert_yaxis()

# Add values near the bars
for bar, value in zip(bars, eu_export_2021['tonne']):
    ax.text(value + 100000, bar.get_y() + bar.get_height()/2,
            f'{value / 1e6:.3f} M', va='center', fontsize=10, color='black')

ax.set_xlim(0, max(eu_export_2021['tonne']) * 1.1)
ax.xaxis.set_visible(False)

# plt.savefig('..//assets//eu_export_2021_by_materials.png', dpi=300)
plt.show()





