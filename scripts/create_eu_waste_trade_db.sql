-- Create the database with character set and collation
create database if not exists eu_waste_trade_db
character set utf8mb4
collate utf8mb4_unicode_ci;

use eu_waste_trade_db;

-- Create a eu-country labels table
drop table if exists eu_country_labels;
create table eu_country_labels (
	country_code varchar(20) primary key,
    country_label varchar(50) not null
);

-- Create a material labels table
drop table if exists material_labels;
create table material_labels (
	material_code varchar(20) primary key,
    material_label varchar(50) not null
);

-- Create a partner labels table - EU and non-EU countries
drop table if exists partner_labels;
create table partner_labels (
	partner_code varchar(20) primary key,
    partner_label varchar(100) not null
);

-- Create a waste export table
drop table if exists waste_export;
create table waste_export (
	material_code varchar(20),
    partner_code varchar(20),
    country_code varchar(20),
    time_period year,
    tonne double,
    thousand_euros double,
    primary key (material_code, partner_code, country_code, time_period),
    
    -- Define a foreign key with CASCADE delete and restrict update
    foreign key (material_code) references material_labels(material_code),
    foreign key (partner_code) references partner_labels(partner_code),
    foreign key (country_code) references eu_country_labels(country_code)
);


-- Create a waste import table
drop table if exists waste_import;
create table waste_import (
	material_code varchar(20),
    partner_code varchar(20),
    country_code varchar(20),
    time_period year,
    tonne double,
    thousand_euros double,
    primary key (material_code, partner_code, country_code, time_period),
    
    -- Define a foreign key with CASCADE delete and restrict update
    foreign key (material_code) references material_labels(material_code),
    foreign key (partner_code) references partner_labels(partner_code),
    foreign key (country_code) references eu_country_labels(country_code)
);



