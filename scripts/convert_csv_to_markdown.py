import pandas as pd

# Load your CSV file
file_path = '..//results//eu_export_by_years_materials.csv'
data = pd.read_csv(file_path)

# Convert to Markdown table
def convert_to_markdown_table(df):
    table = "| " + " | ".join(df.columns) + " |\n"
    table += "| " + " | ".join(["-" * len(col) for col in df.columns]) + " |\n"
    for _, row in df.iterrows():
         # Use a generator to check data types and format accordingly
        formatted_row = [
            f"{int(value)}" if isinstance(value, (int, float)) and value.is_integer() else str(value)
            for value in row
        ]
        table += "| " + " | ".join(formatted_row) + " |\n"
    return table

markdown_table = convert_to_markdown_table(data)

# Save to a .md file or print
output_path = '..//results//eu_export_by_years_materials.md'
with open(output_path, 'w') as f:
    f.write(markdown_table)

print(markdown_table)  # Print to verify
