with customer_orders_count as (
	select customer_id, 
		count(*) as Total_Orders
	from (select * from orders where order_date >= now() - interval 90 day) three_months_data
	group by customer_id
),
customer_classification as (
	select customer_id,
		case
			when Total_Orders = 1 then 'One-Time Customer'
            else 'Repeat Customer'
		end as customer_type
	from customer_orders_count
)
select customer_type,
	count(*) as `Count`,
    round(100.0 * count(*)/ (select count(*) from customer_orders_count),2) as Percentage
from customer_classification
group by customer_type;