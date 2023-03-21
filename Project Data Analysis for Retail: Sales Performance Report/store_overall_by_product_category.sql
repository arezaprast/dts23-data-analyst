select 
  year(order_date) as years, product_sub_category, sum(sales) as sales
from 
  dqlab_sales_store
where 
  order_status = 'Order Finished' and
  (year(order_date) between '2011' and '2012')
group by 
  year(order_date), product_sub_category
order by
  years asc, sales desc;
