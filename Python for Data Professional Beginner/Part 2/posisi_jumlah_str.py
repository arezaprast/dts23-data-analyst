teks = "Apel malang adalah apel termanis dibanding apel - apel lainnya"
# Fitur .find()
# Mengembalikan posisi dari sebuah teks (sub - string) 
#  lainnya dalam sebuah string
print(">>> Fitur .find()")
print(teks.find("Apel"))
print(teks.find("malang"))

# Fitur .count()
# Menghitung jumlah kemunculan sebuah teks (string) lainnya 
#  dalam suatu string (string yang dicari bersifat case sensitive).
print(">>> Fitur .count()")
kemunculan_kata_apel = teks.count("apel")
print(kemunculan_kata_apel)
