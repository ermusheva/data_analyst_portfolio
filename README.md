# EU Waste Trade Analysis (2004–2021)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)

## Project Description
This project analyzes the trade of waste the European Union with non-EU countries from 2004 to 2021. The analysis includes waste import and export data measured in tonnes and thousands of euros. Data source is [Kaggle dataset from Original Eurostat data](https://www.kaggle.com/datasets/konradb/european-waste-export-2004-2020/data?select=aggregate_trash.csv).

The data used in this project is provided under the CC0 1.0 Universal (Public Domain Dedication) license. This means the data is free to use, share, and adapt without restriction. 

The project workflow involves cleaning the data with python, organizing it into a MySQL database, performing preliminary data exploration, .


<details>
  <summary>Click to view workflow</summary>

## Workflow
### 0. **Extract all from data.zip to a new folder 'data'**

### 1. **Review and clean CSV Files**
- Execute the python script `divide_aggregate_trash.py`
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
- Execute the script `select_eu_waste_trade_db.sql` to compute key metrics.
  
</details>

## Results and Insights
### 1. Total Export and Import Waste Trade of EU with Non-EU Countries (2004–2021)
- **Description:** Total tonnes of waste exported and imported each year.
- **Query File:** [tbd.sql](tbd)
- **Result Table:**

| time_period | export_tonne | export_thousand_euros | import_tonne | import_thousand_euros |
| ----------- | ------------ | --------------------- | ------------ | --------------------- |
| 2004 | 18655562 | 5039013.6 | 17708518 | 5579673.9 |
| 2005 | 18832230 | 6010143.7 | 17354622 | 5862903.7 |
| 2006 | 19692837 | 8166535.6 | 18041614 | 9276452.5 |
| 2007 | 21328843 | 9524820.4 | 16993218 | 10403432.8 |
| 2008 | 24377567 | 10001894.8 | 16703767 | 10077037.9 |
| 2009 | 29778786 | 8797932.1 | 15156227 | 5747534.2 |
| 2010 | 30209184 | 13192256.9 | 17695080 | 9529343.2 |
| 2011 | 31184664 | 15710445.5 | 18414289 | 11845246.4 |
| 2012 | 31934020 | 15653122.2 | 14776790 | 11018539.8 |
| 2013 | 27807551 | 12322876.1 | 14937692 | 10161340.8 |
| 2014 | 28389290 | 11724045.5 | 15305226 | 9504259.2 |
| 2015 | 25718417 | 10380729.7 | 15492087 | 9103496.1 |
| 2016 | 29231567 | 9995842.4 | 17106115 | 8934971.5 |
| 2017 | 30995793 | 12425160.7 | 19060531 | 9698732.2 |
| 2018 | 30940770 | 13103782 | 17121800 | 12145856.7 |
| 2019 | 30905938 | 13389584.7 | 16758875 | 12847212.8 |
| 2020 | 32807186 | 12961870.8 | 16008408 | 13467221.3 |
| 2021 | 32983442 | 20014174.6 | 19746409 | 19011603.7 |

- **Visualization:**  
  ![tbd](tbd.png)

## Useful Links
- [Project Repository](https://github.com/ermusheva/eu_waste_trade)
- [Download the Dataset](https://www.kaggle.com/datasets/konradb/european-waste-export-2004-2020/data)
- [Contact Me](mailto:ermusheva@gmail.com)
