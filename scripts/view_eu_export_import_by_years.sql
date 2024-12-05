use eu_waste_trade_db;

-- View: eu_export_by_years_materials
-- Description:
--   Aggregates total waste import and export of the EU by year.
-- Columns:
--   time_period: The year of the data.
--   export_tonne: Total exported waste in tonnes.
--   export_thousand_euros: Total export value in thousand euros.
--   import_tonne: Total imported waste in tonnes.
--   import_thousand_euros: Total import value in thousand euros.
create or replace view eu_export_import_by_years as
with export_by_years (time_period, export_tonne, export_thousand_euros) as (
	select
		time_period,
		tonne,
        thousand_euros
	from waste_export
    where country_code = 'EU27_2020'
    and material_code = 'TOTAL'
    and partner_code = 'EXT_EU27_2020'
),
import_by_years (time_period, import_tonne, import_thousand_euros) as (
	select
		time_period,
		tonne,
        thousand_euros
	from waste_import
    where country_code = 'EU27_2020'
    and material_code = 'TOTAL'
    and partner_code = 'EXT_EU27_2020'
)
select *
from export_by_years as e
left join import_by_years as i
using (time_period)
order by time_period;

select * from eu_export_import_by_years;