# Fitur .clear()
# Mengembalikan copy dari setiap elemen dalam set.
#  Serupa dengan fitur copy() pada tipe data collections lainnya,
#   fitur copy() tidak akan mengubah nilai 
#    dari elemen asal seperti fungsi assignment.
print(">>> Fitur .clear()")
info_karyawan = {'nama' : 'Aksara', 'nik' : '1211011', 
'pekerjaan' : 'Data Analyst'}
info_karyawan.clear()
print(info_karyawan)

# Fitur .copy()
# Mengembalikan copy dari setiap elemen dalam set.
#  Serupa dengan fitur copy() pada tipe data collections lainnya,
#   fitur copy() tidak akan mengubah nilai dari elemen asal 
#    seperti fungsi assignment.
print(">>> Fitur .copy()")
info_karyawan1 = {'nama' : 'Aksara', 'nik' : '1211011',
'pekerjaan' : 'Data Analyst'}
info_karyawan2 = info_karyawan1.copy()
info_karyawan2['nama'] = 'Senja'
info_karyawan2['nik'] = '1211056'
print(info_karyawan1)
print(info_karyawan2)

# Fitur .keys()
# Mengembalikan list dari seluruh kunci akses ("key") 
#  dari setiap elemen dalam sebuah dictionary.
print(">>> Fitur .keys()")
info_karyawan = {'nama' : 'Aksara', 'nik' : '1211011',
'pekerjaan' : 'Data Analyst'}
kunci_akses = list(info_karyawan.keys())
print(kunci_akses)

# Fitur .values()
# Mengembalikan list dari seluruh nilai ("value") 
#  dari setiap elemen dalam sebuah dictionary.
print(">>> Fitur .values()")
value_dict = list(info_karyawan.values())
print(value_dict)

# Fitur .update()
# Menambahkan kunci akses ("key") dan nilai baru 
#  ("value") ke dalam sebuah dictionary.
print(">>> Fitur .update()")
info_karyawan.update({'skillset':['Python', 'R']})
print(info_karyawan)
