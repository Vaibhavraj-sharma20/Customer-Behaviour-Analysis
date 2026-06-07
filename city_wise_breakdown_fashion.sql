create temporary table req_orders as
select *
from orders 
where order_date >= now() - interval 30 day;

select city,
	count(order_id) as Total_Orders,
    round(sum(revenue),2) as Total_Revenue,
    round(avg(revenue),2) as AOV
from req_orders o
join products p
on o.product_id = p.product_id
where category = 'Fashion'
group by city;