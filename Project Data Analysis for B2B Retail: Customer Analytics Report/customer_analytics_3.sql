select
  left(productCode, 3) as categoryid,
  count(distinct orderNumber) as total_order,
  sum(quantity) as total_penjualan
from
  (select 
    productCode, orderNumber, quantity, status 
   from 
    orders_2) as tabel_c
where
  status = 'Shipped'
group by
  categoryid
order by
  total_order desc;
