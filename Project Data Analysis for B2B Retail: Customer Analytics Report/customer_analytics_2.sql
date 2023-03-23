select
	quarter, 
	count(distinct customerID) as total_customers
from 
	(select 
	  customerID, createDate, quarter(createDate) as quarter
	from 
	  customer 
	where 
	  createDate between '2004-01-01' and '2004-06-30')
	as tabel_b
where
	customerID in 
	(select distinct 
	  customerID 
	 from 
	  orders_1
	union
	select distinct 
	  customerID 
	from 
	  orders_2)
group by 
	quarter;
