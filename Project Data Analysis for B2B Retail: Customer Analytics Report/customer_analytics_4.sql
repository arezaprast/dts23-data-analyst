#Menghitung total unik customers yang transaksi di quarter_1
SELECT 
  COUNT(DISTINCT customerID) as total_customers 
FROM 
  orders_1;
#output = 25
select 
  1 as quarter, 
  round(count(distinct customerid)*100/25,4) as Q2
from 
  orders_1
where 
  customerid in (select distinct customerid from orders_2);
