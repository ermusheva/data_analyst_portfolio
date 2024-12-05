use eu_waste_trade_db;

-- View: eu_export_by_years_materials
-- Description:
--   Summarizes total EU waste exports by year and material type.
-- Columns:
--   time_period: The year of the data.
--   material_label: Type of waste material.
--   tonne: Total exported waste in tonnes.
--   percent_of_year_total: Percentage of the material's exports relative to the yearly total.
create or replace view eu_export_by_years_materials as
with eu_export_by_materials_years as (
	select 
		time_period,
		material_code,
		sum(tonne) over (partition by time_period) as year_total,
		tonne
	from waste_export
	where country_code = 'EU27_2020'
	and partner_code = 'EXT_EU27_2020'
	and material_code != 'TOTAL'
)
select 
	time_period, 
    replace(material_label, '\r', '') as material_label, 
    tonne,
    if(year_total!=0, round(100*tonne/year_total, 2), 0) as percent_of_year_total
from eu_export_by_materials_years
left join material_labels
using (material_code)
order by time_period, tonne desc;

select * from eu_export_by_years_materials;

