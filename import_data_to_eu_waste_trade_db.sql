-- Import data from csv-files to tables in eu_waste_trade_db
-- Before the script is executed all csv-files 'geo_labels.csv', 'material_labels.csv', 'partner_labels.csv', 'import_trash.csv', 'export_trash.csv' should be placed in the directory, defined in variable 'secure-file-priv'.


use eu_waste_trade_db;

load data infile 'c:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\geo_labels.csv'
into table eu_country_labels
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

load data infile 'c:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\material_labels.csv'
into table material_labels
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

load data infile 'c:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\partner_labels.csv'
into table partner_labels
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

load data infile 'c:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\export_trash.csv'
into table waste_export
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

load data infile 'c:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\import_trash.csv'
into table waste_import
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
