select * 
from tabel_A
where kode_pelanggan = 'dqlabcust03'
union
select * 
from tabel_B
where kode_pelanggan = 'dqlabcust03';
