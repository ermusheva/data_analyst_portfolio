



# EU Waste Trade Analysis (2004–2021)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)


## Project Description

<p align="right">
  <img src="assets/waste_trade_img.jpg" alt="Waste Trade" width="350" align="right"  style="margin-left: 0px;">
</p>

This project analyzes the trade of waste the European Union with non-EU countries from 2004 to 2021. The analysis includes waste import and export data measured in tonnes and thousands of euros. Data source is [Kaggle dataset from Original Eurostat data](https://www.kaggle.com/datasets/konradb/european-waste-export-2004-2020/data?select=aggregate_trash.csv).

The data used in this project is provided under the CC0 1.0 Universal (Public Domain Dedication) license. This means the data is free to use, share, and adapt without restriction. 

The project workflow involves cleaning the data with Python, organizing it into a MySQL database, performing preliminary data exploration, and visualization in Python and Flourish.

<details>
  <summary>Click to view workflow</summary>


## Workflow
### 0. **Extract all from data.zip to a new folder \data**

### 1. **Review and clean CSV Files**
- Execute the Python script `divide_aggregate_trash.py`
  - Remove trades of materials and partners subcategories to avoid aggregation conflicts.
  - Split `aggregate_trash.csv` into two files: `import_trash.csv` and `export_trash.csv`.
  - Pivot original data to reduce number of trade raws. Final files contain waste trade values in tonnes and thousands of euros, categorized by material, partner country, EU country, and year.

### 2. **Create Database and Tables**
- Execute the SQL script `create_eu_waste_trade_db.sql` to create the database structure and tables.

### 3. **Import Data**
- Place the following CSV files in the directory defined by the `secure-file-priv` variable in MySQL:
  - `geo_labels.csv`
  - `material_labels.csv`
  - `partner_labels.csv`
  - `import_trash.csv`
  - `export_trash.csv`
- Execute the script `import_data_to_eu_waste_trade_db.sql` to import the data into the corresponding tables.

### 4. **Check Data**
- Manually compare selected values by countries, years in the MySQL database against the original data on [Eurostat data](https://ec.europa.eu/eurostat/databrowser/view/ENV_WASTRDMP__custom_6104729/).

### 5. **Optimize Tables**
- Execute the script `alter_eu_waste_trade_db.sql` to add indexes to the database tables.

### 6. **Analyze Data**
- Execute scripts to compute key metrics:
  - `view_eu_export_import_by_years.sql`
  - `view_eu_export_by_years_materials.sql`
  - `proc_top_n_export_partners_of_country_by_years.sql`


### 7. **Export Data**
- Export data to csv-files with the help of MySQL Workbench and place them in \results folder.
  - `eu_export_import_by_years.csv`
  - `eu_export_by_years_materials.csv`
  - `top_10_export_partners_by_years.csv`

### 8. **Visualize Data in Python**
- Execute Python scripts to visualize data and save results:
  - `visual_eu_export_import_by_years.py`
  - `visual_eu_export_by_years_materials.py`
  - `pivot_top_10_export_partners_by_years.py`
    
### 9. **Visualize in Flourish**
- Add to data `eu_top_10_export_partners.csv` image urls of country flags from Flourich with the help of Google Sheets.
- Load data to Flourish.
- Set animation parameters in Flourish.

  
</details>

## Results
### 1. Total Export and Import Waste Trade of EU with Non-EU Countries (2004–2021)
- **Description:** Total tonnes of waste exported and imported each year.
- **Query File:** [tbd.sql](tbd)
- **Result Table:**

| time_period | export_tonne | export_thousand_euros | import_tonne | import_thousand_euros |
| ----------- | ------------ | --------------------- | ------------ | --------------------- |
| 2004 | 18655562 | 5039013.6 | 17708518 | 5579673.9 |
| 2005 | 18832230 | 6010143.7 | 17354622 | 5862903.7 |
...
| 2020 | 32807186 | 12961870.8 | 16008408 | 13467221.3 |
| 2021 | 32983442 | 20014174.6 | 19746409 | 19011603.7 |

- **Visualization:**  
  ![tbd](tbd.png)

## Useful Links
- [Project Repository](https://github.com/ermusheva/eu_waste_trade)
- [Download the Dataset](https://www.kaggle.com/datasets/konradb/european-waste-export-2004-2020/data)
- [Contact Me](mailto:ermusheva@gmail.com)
