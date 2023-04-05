select CustomerName, ContactName, City, PostalCode 
from Customers
union
select SupplierName, ContactName, City, PostalCode 
from Suppliers; 
