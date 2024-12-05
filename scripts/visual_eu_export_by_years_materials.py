import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import squarify

def add_legend(ax, labels, values, colors, title='', loc="upper left", bbox_to_anchor=(1, 1)):
    """
    Adds a legend to the given axis with labels, values, and colors.

    Parameters:
    - ax: The axis object where the legend will be added.
    - labels: List of category labels.
    - values: List of corresponding values for the categories.
    - colors: List of colors used in the treemap.
    - title: Title of the legend (default is "Legend (with values)").
    - loc: Location of the legend (default is "upper left").
    - bbox_to_anchor: Positioning of the legend relative to the plot (default is (1, 1)).
    """
    # Format labels to include values
    legend_labels = [f"{label}\n{value}" for label, value in zip(labels, values)]
    
    # Create marker patches for the legend
    legend_patches = [
        plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10)
        for color in colors
    ]
    
    # Add the legend to the axis
    ax.legend(legend_patches, legend_labels, title=title, loc=loc, bbox_to_anchor=bbox_to_anchor)


# Load result csv file
eu_export_by_materials = pd.read_csv('..//results//eu_export_by_years_materials.csv')

eu_export_2021 = eu_export_by_materials[eu_export_by_materials['time_period'] == 2021]
# Replace material names to shorter names
eu_export_2021.loc[:, 'material_label'] = eu_export_2021['material_label'].replace('Not specified', 'Not spec.');
eu_export_2021.loc[:, 'material_label'] = eu_export_2021['material_label'].replace('Paper and cardboard', 'Paper');
print(eu_export_2021.head())
print(len(eu_export_2021))

# Define a colormap
num_materials = len(eu_export_2021)
cmap = plt.get_cmap("plasma", num_materials)
colors = cmap(range(num_materials))


fig, ax = plt.subplots(figsize=(10, 6))
squarify.plot(sizes=eu_export_2021['tonne'], 
              label=eu_export_2021['material_label'], 
              alpha=.8, 
              pad = 1,
              color = colors,
              text_kwargs={'color':'white'})

plt.axis('off')
ax.set_title('Total export of the European Union in 2021 by materials, Tonnes')
add_legend(ax, 
           eu_export_2021['material_label'], 
           eu_export_2021['tonne'], 
           colors, 
           loc='best')

plt.tight_layout()
plt.savefig('..//assets//eu_export_2021_by_materials.png', dpi=300)
plt.show()





