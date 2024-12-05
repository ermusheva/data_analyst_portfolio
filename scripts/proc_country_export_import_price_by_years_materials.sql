use eu_waste_trade_db;

-- Compare waste export and import by country by waste types and years
DROP procedure IF EXISTS `country_export_import_price_by_years_materials`;
DELIMITER $$
CREATE PROCEDURE `country_export_import_price_by_years_materials` (in in_country_code varchar(20))
BEGIN
with country_export_waste as (
	select 
		time_period,
        material_code,
        partner_code,
        country_code,
		tonne as export_tonne,
		thousand_euros as export_thousand_euros,
        round(if(tonne > 0, (1000*thousand_euros)/tonne, 0), 2) as export_price
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
        round(if(tonne > 0, (1000*thousand_euros)/tonne, 0), 2) as import_price
	from waste_import
	where country_code = in_country_code
    and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
    and material_code != 'TOTAL'
)
select
	time_period,
    replace(material_label, '\r', '') as material_label,
    partner_code,
    export_tonne,
    export_thousand_euros,
	export_price,
    import_tonne,
    import_thousand_euros,
    import_price
from country_export_waste as e
left join country_import_waste as i
using (time_period, material_code, country_code, partner_code)
left join material_labels as m
using (material_code);
END$$
DELIMITER ;


CALL `country_export_import_price_by_years_materials`('DE');

CALL `country_export_import_price_by_years_materials`('ES');