select 
  year(order_date) as years, sum(sales) as sales, sum(discount_value) as promotion_value,
  round((sum(discount_value)/sum(sales))*100,2) as burn_rate_percentage
from 
  dqlab_sales_store
where 
  order_status = 'Order Finished'
group by 
  year(order_date)
order by 
  years asc;
