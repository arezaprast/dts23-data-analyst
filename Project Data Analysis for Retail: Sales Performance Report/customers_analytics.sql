select 
  year(order_date) as years, count(distinct customer) as number_of_customer
from 
  dqlab_sales_store
where 
  order_status = 'Order Finished'
group by 
  years
order by 
  years;
