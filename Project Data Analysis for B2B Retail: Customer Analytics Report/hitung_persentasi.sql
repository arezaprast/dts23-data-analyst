select 
  quarter, sum(quantity) as total_penjualan, 
  sum(quantity*priceeach) as revenue
from 
  (select 
      orderNumber, status, quantity, priceeach, 
      '1' as quarter from orders_1 
   where 
      status = 'Shipped'
   union
   select 
      orderNumber, status, quantity, priceeach, 
      '2' as quarter from orders_2 
   where 
      status = 'Shipped'
  ) as tabel_a
group by 
  quarter;
