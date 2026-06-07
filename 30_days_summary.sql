with last_30_days_orders as (
	select *
	from orders o
	where order_date >= now() - INTERVAL 30 DAY
	)
select count(*) as Total_Orders,
	round(sum(revenue),2) as Revenue,
    round(avg(revenue),2) as AOV
from last_30_days_orders;