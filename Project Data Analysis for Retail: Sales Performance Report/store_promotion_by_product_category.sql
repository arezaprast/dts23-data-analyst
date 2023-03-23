select 
  year(order_date) as years, 
  product_sub_category, 
  product_category, sum(sales) as sales, 
  sum(discount_value) as promotion_value, 
  round(sum(discount_value)/sum(sales)*100,2) as burn_rate_percentage
from 
  dqlab_sales_store
where 
  year(order_date) = '2012' and order_status = 'Order Finished'
group by 
  year(order_date), 
  product_sub_category,
  product_category
order by 
  years, 
  sales desc;
