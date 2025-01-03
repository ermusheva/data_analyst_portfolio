use eu_waste_trade_db;

-- All export history of top N by sum export partners for EU country by years
DROP procedure IF EXISTS `top_n_sum_export_partners_of_country_by_years`;
DELIMITER $$
-- Procedure: top_n_sum_export_partners_of_country_by_years
-- Input: 
--   in_country_code (VARCHAR(20)) - code of the EU-country.
--   top_n (INT) - Number of top partners to return.
-- Output: 
--   Returns all export of top N partners (non-EU) by year with columns:
--     partner_label, time_period, total_by_all_partners, thousand_euros.
-- Description:
--   Retrieves top N non-EU export partners for the given country - choose N partners with sum max export by period 2004-2021
-- and returns export of these countries by years 2004-2021 by all materials for the given country
CREATE PROCEDURE `top_n_sum_export_partners_of_country_by_years` (in in_country_code varchar(20), in top_n int)
BEGIN
	with country_export_top_partners as (
		select 
			partner_code as partner_code,
			sum(thousand_euros) as year_total
		from waste_export
		where material_code = 'TOTAL'
		and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
        and country_code = in_country_code
        group by partner_code
        order by year_total desc limit top_n
	),
    export_partners as (
    select 
		partner_code,
        time_period,
        thousand_euros
	from waste_export
    where material_code = 'TOTAL'
		and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
        and country_code = in_country_code
    ),
    export_by_years as (
		select
			time_period,
			thousand_euros
		from waste_export
		where country_code = in_country_code
			and material_code = 'TOTAL'
			and partner_code = 'EXT_EU27_2020'
    )
	select 
		replace(partner_label, '\r', '') as partner_label,
        ep.time_period,
        e.thousand_euros as total_by_all_partners,
		ep.thousand_euros
	from country_export_top_partners as t
    left join partner_labels as l
    using (partner_code)
    join export_partners as ep
	on (t.partner_code = ep.partner_code)
    join export_by_years as e
    on (e.time_period = ep.time_period);
END$$
DELIMITER ;

-- Top 5 partners for Germany waste export
call `top_n_sum_export_partners_of_country_by_years`('DE', 5);
-- Top 10 partners for Spain waste export
call `top_n_sum_export_partners_of_country_by_years`('ES', 10);
-- Top 10 partners for EU waste export
call `top_n_sum_export_partners_of_country_by_years`('EU27_2020', 10);