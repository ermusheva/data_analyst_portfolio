import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Format the y-axis to show values in billions
def to_billions(y, pos):
    return f'{y / 1e6:.1f}B'


# Load result csv file
top_n_eu_export = pd.read_csv('..//results//top_10_sum_export_partners_EU_by_years.csv')
top_n_eu_export.loc[:, 'partner_label'] = top_n_eu_export['partner_label'].replace('China including Hong Kong', 'China');
top_n_eu_export.loc[:, 'partner_label'] = top_n_eu_export['partner_label'].replace('Turkiye', 'Turkey');

partners = top_n_eu_export['partner_label'].unique();
num_partners = len(partners);

# Set up the figure and axis
num_axs_x = 3
num_axs_y = int(np.ceil(num_partners / num_axs_x))
fig, axs = plt.subplots(num_axs_y, num_axs_x, figsize=(16, 9), sharex=True, sharey=True, constrained_layout=True)

# Define a colormap
cmap = plt.get_cmap("plasma", 2)

for i in range(0, num_partners):
    partner = partners[i]
    partner_data = top_n_eu_export[(top_n_eu_export.loc[:, 'partner_label'] == partner)]
    years = partner_data['time_period']
    axs[i % num_axs_y, i // num_axs_y].plot(years, partner_data['thousand_euros'], color=cmap(0))
    axs[i % num_axs_y, i // num_axs_y].set_title(partner, loc="left", fontfamily='sans-serif')
    plt.xticks(years[1:len(years):2], fontfamily='sans-serif')
    axs[i % num_axs_y, i // num_axs_y].yaxis.set_major_formatter(FuncFormatter(to_billions))


title_str = 'Top ' + str(num_partners) + ' export partners of the European Union by years, Billions \N{euro sign}'
fig.suptitle(title_str, fontsize=16, fontweight="bold", fontfamily='sans-serif')
plt.savefig('..//assets//top_10_sum_export_partners_EU_by_years.png', dpi=300)
plt.show()



