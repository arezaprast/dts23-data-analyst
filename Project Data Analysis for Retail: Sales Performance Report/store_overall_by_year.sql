select 
	year(order_date) as years, sum(sales) as sales,
	count(order_quantity) as number_of_order
from 
	dqlab_sales_store
where 
	order_status = 'Order Finished'
group by 
	years
order by 
	years asc;
