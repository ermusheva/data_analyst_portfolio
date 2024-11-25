# EU Waste Trade Analysis (2004–2021)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

## Project Description
This project analyzes the trade of waste the European Union from 2004 to 2021. The analysis includes waste import and export data measured in tonnes and thousands of euros. Data source is [Kaggle dataset from Original Eurostat data](https://www.kaggle.com/datasets/konradb/european-waste-export-2004-2020/data?select=aggregate_trash.csv).

The data used in this project is provided under the CC0 1.0 Universal (Public Domain Dedication) license. This means the data is free to use, share, and adapt without restriction. 

The project workflow involves cleaning the data, organizing it into a MySQL database, and performing preliminary data exploration.

## Workflow
### 0. **Extract data from data.zip**

### 1. **Examine CSV Files**
- **Task:** Review and clean the provided CSV files.
- **Steps:**
  - Remove all "Total" values to avoid aggregation conflicts.
  - Split `aggregate_trash.csv` into two files: `import_trash.csv` and `export_trash.csv`. These files contain waste trade values in tonnes and thousands of euros, categorized by material, partner country, EU country, and year.
- **Script:** `divide_aggregate_trash.py`

### 2. **Create Database and Tables**
- **Task:** Set up a MySQL database to store and organize the data.
- **Steps:**
  - Execute the SQL script `create_eu_waste_trade_db.sql` to create the database structure and tables.

### 3. **Import Data**
- **Task:** Load the cleaned data into the MySQL database.
- **Steps:**
  - Place the following CSV files in the directory defined by the `secure-file-priv` variable in MySQL:
    - `geo_labels.csv`
    - `material_labels.csv`
    - `partner_labels.csv`
    - `import_trash.csv`
    - `export_trash.csv`
  - Execute the script `import_data_to_eu_waste_trade_db.sql` to import the data into the corresponding tables.

### 4. **Check Data**
- **Task:** Verify the accuracy of the imported data.
- **Steps:**
  - Manually compare selected values by countries, years in the MySQL database against the original data on [Eurostat data](https://ec.europa.eu/eurostat/databrowser/view/ENV_WASTRDMP__custom_6104729/).

### 5. **Optimize Tables**
- **Task:** Improve database performance by creating indexes.
- **Steps:**
  - Execute the script `alter_eu_waste_trade_db.sql` to add indexes to the database tables.

### 6. **Analyze Data**
- **Task:** Perform basic queries to extract insights from the data.
- **Steps:**
  - Execute the script `select_eu_waste_trade_db.sql` to compute key metrics.
