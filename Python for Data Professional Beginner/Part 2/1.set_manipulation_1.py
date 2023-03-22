# Fitur .add()
#   Menambahkan data ke dalam set. Penting untuk kita ingat bahwa pada 
#   tipe data set tidak mengizinkan adanya duplikasi elemen di dalamnya
print(">>> Fitur .add()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.add('Melon')
print(set_buah)
# Fitur .clear()
#   Menghapus seluruh elemen dalam sebuah set
print(">>> Fitur .clear()")
set_buah = {'Jeruk','Apel','Anggur'}
set_buah.clear
print(set_buah)
# Fitur .copy()
#   Mengembalikan copy dari setiap elemen dalam set
print(">>> Fitur .copy()")
set_buah1 = {'Jeruk','Apel','Anggur'}
set_buah2 = set_buah1
set_buah3 = set_buah1.copy()
set_buah2.add('Melon')
set_buah3.add('Kiwi')
print(set_buah1)
print(set_buah2)
# Fitur .update()
#   Menambahkan elemen dari suatu set dengan set lainnya
print(">>> Fitur .update()")
parcel1 = {'Anggur','Apel','Jeruk'}
parcel2 = {'Apel','Kiwi','Melon'}
parcel1.update(parcel2)
print(parcel1)
# Fitur .pop()
#   Menghilangkan elemen dari sebuah set secara acak
print(">>> Fitur .pop()")
parcel = {'Anggur','Apel','Jeruk'}
buah = parcel.pop()
print(buah)
print(parcel)
# Fitur .remove()
#   Menghilangkan elemen dengan nilai tertentu
print(">>> Fitur .remove()")
parcel = {'Anggur','Apel','Jeruk'}
parcel.remove('Apel')
print(parcel)
