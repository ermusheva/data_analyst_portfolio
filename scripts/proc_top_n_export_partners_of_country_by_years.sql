use eu_waste_trade_db;

-- Top N export partners for EU country by years
DROP procedure IF EXISTS `top_n_export_partners_of_country_by_years`;
DELIMITER $$
-- Procedure: top_n_export_partners_of_country_by_years
-- Input: 
--   in_country_code (VARCHAR(20)) - code of the EU-country.
--   top_n (INT) - Number of top partners to return.
-- Output: 
--   Returns top export partners (non-EU) by year with columns:
--     time_period, partner_label, thousand_euros, percent_of_year_total.
-- Description:
--   Retrieves top N non-EU export partners for the given country and calculates
--   their share as a percentage of the total exports for each year.
CREATE PROCEDURE `top_n_export_partners_of_country_by_years` (in in_country_code varchar(20), in top_n int)
BEGIN
	with country_export_partners as (
		select 
			time_period,
			partner_code,
			thousand_euros,
			dense_rank() over(partition by time_period order by thousand_euros desc) as euro_rank,
			round(sum(thousand_euros) over(partition by time_period), 2) as year_total
		from waste_export
		where country_code = in_country_code
		and material_code = 'TOTAL'
		and partner_code not in ('INT_EU27_2020', 'EXT_EU27_2020')
		order by time_period, euro_rank
	)
	select 
		time_period,
		replace(partner_label, '\r', '') as partner_label,
		thousand_euros,
		if(year_total!=0, round(100*thousand_euros/year_total, 2), 0) as percent_of_year_total
	from country_export_partners
	left join partner_labels 
	using (partner_code)
	where euro_rank < (top_n+1);
END$$
DELIMITER ;

-- Top 5 partners for Germany waste export
call `top_n_export_partners_of_country_by_years`('DE', 5);
-- Top 10 partners for Spain waste export
call `top_n_export_partners_of_country_by_years`('ES', 10);
-- Top 10 partners for EU waste export
call `top_n_export_partners_of_country_by_years`('EU27_2020', 10);