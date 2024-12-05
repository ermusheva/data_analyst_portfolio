use eu_waste_trade_db;

alter table waste_export
	add index (material_code, partner_code, country_code);

alter table waste_import
	add index (material_code, partner_code, country_code);

alter table waste_export
	add index (material_code, partner_code, country_code);

alter table waste_import
	add index (material_code, time_period);

alter table waste_import
	add index (material_code, time_period, country_code);
    
alter table waste_export
	add index (material_code, time_period, country_code);

alter table waste_export
	add index (material_code, time_period);


