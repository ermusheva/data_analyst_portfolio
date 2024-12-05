use eu_waste_trade_db;

-- Compare waste export and import by country by waste types and years
DROP procedure IF EXISTS `country_export_import_by_materials_years`;
DELIMITER $$
CREATE PROCEDURE `country_export_import_by_materials_years` (in in_country_code varchar(20))
BEGIN
with country_export_waste as (
	select 
		time_period,
        material_code,
        partner_code,
        country_code,
		tonne as export_tonne,
		thousand_euros as export_thousand_euros,
        if(tonne > 0, thousand_euros/tonne, 0) as export_price
	from waste_export
	where country_code = in_country_code
    and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
    and material_code != 'TOTAL'
),
country_import_waste as (
	select 
		time_period,
        material_code,
        country_code,
        partner_code,
		tonne as import_tonne,
		thousand_euros as import_thousand_euros,
        if(tonne > 0, thousand_euros/tonne, 0) as import_price
	from waste_import
	where country_code = in_country_code
    and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
    and material_code != 'TOTAL'
)
select
	time_period,
    replace(material_label, '\r', '') as material_label,
    sum(export_tonne) as sum_export_tonne,
    round(sum(export_thousand_euros), 2) as sum_export_ths_euros,
	round(avg(export_price), 2) as avg_export_price,
    sum(import_tonne) as sum_import_tonne,
    round(sum(import_thousand_euros), 2) as sum_import_ths_euros,
    round(avg(import_price), 2) as avg_import_price
from country_export_waste as e
left join country_import_waste as i
using (time_period, material_code, country_code, partner_code)
left join material_labels as m
using (material_code)
group by material_code, time_period
order by material_code, time_period;
END$$
DELIMITER ;


CALL `country_export_import_by_materials_years`('DE');

CALL `country_export_import_by_materials_years`('ES');