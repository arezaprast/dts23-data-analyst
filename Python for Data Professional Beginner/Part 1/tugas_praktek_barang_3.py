contoh_list = ['dewi', 'budi', 'cici', 'linda', 'cici']
print(contoh_list)
contoh_set = ('dewi', 'budi', 'cici', 'linda', 'cici')
print(contoh_set)
contoh_frozen_set = ({'dewi', 'budi', 'cici', 'linda', 'cici'})
print(contoh_frozen_set)

'''Tipe data set diawali dengan tanda kurung buka kurawal ( { ), memisahkan setiap elemen di dalamnya dengan tanda koma ( , ) 
dan ditutup dengan tanda kurung tutup ( } ). Namun berbeda dengan tipe data sequence, seperti list, 
tipe data objek tidak mengizinkan adanya elemen dengan nilai yang sama dan tidak memperdulikan urutan dari elemen.
Tipe data frozenset sebenarnya hanya merupakan set yang bersifat immutable, 
yang artinya setiap elemen di dalam frozenset tidak dapat diubah setelah proses deklarasinya.
Dari kedua contoh output pada program, dapat terlihat:
1. Berbeda dengan tipe data set, tipe data list memperdulikan urutan dari setiap elemen saat list dideklarasikan.
2. Berbeda dengan list yang mengizinkan adanya duplikasi elemen, tipe data set tidak mengizinkan adanya elemen dengan nilai yang sama di dalamnya. 
'''
