# Fitur .index()
# Mengembalikan indeks dari elemen pertama yang ditemukan 
#  dari awal sebuah list
print(">>> Fitur .index()")
list_score = ['Budi','Sud','Budi','Budi','Budi','Sud','Sud']
score_pertama_sud = list_score.index('Sud') + 1
print(score_pertama_sud) # akan menampilkan output 2

# Fitur .insert()
# Menyisipkan elemen pada indeks yang dispesifikasikan
print(">>> Fitur .insert()")
list_score = ['Budi','Sud','Budi','Budi','Sud']
list_score.insert(3, 'Sud')
print(list_score)

# Fitur .pop()
# Menghilangkan elemen pada posisi tertentu
print(">>> Fitur .pop()")
list_menu = ['Gado - gado', 'Ayam Goreng', 'Rendang']
list_menu.pop(1)
print(list_menu)

# Fitur .remove()
# Menghilangkan elemen dengan nilai tertentu
print(">>> Fitur .remove()")
list_menu = ['Gado - gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.remove('Rendang')
print(list_menu)

# Fitur .reverse()
# Membalik urutan elemen dari sebuah list
print(">>> Fitur .reverse()")
list_menu = ['Gado - gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.reverse()
print(list_menu)

# Fitur .sort()
# Mengurutkan elemen pada sebuah list, secara default dengan 
#  urutan dari kecil ke besar (ascending)
print(">>> Fitur .sort()")
list_menu = ['Gado-gado', 'Ayam Goreng', 'Rendang', 'Ketoprak']
list_menu.sort() # Default: Ascending
print(list_menu) 
list_menu.sort(reverse = True) # Descending
print(list_menu) 
