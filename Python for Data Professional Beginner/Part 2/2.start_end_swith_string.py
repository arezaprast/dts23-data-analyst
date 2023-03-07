# Fitur .startswith()
# Mengembalikan nilai kebenaran True ketika sebuah teks (string) 
#  diawali dengan sebuah teks lainnya.
print(">>> Fitur .startswith()")
teks = "Apel malang adalah apel termanis dibanding apel - apel lainnya"
print(teks.startswith("Apel"))
print(teks.startswith("apel"))

# Fitur .endswith()
# Mengembalikan nilai kebenaran True ketika sebuah teks (string) 
#  diakhiri dengan sebuah teks lainnya.
print(">>> Fitur .endswith()")
print(teks.endswith("lainnya"))
print(teks.endswith("apel"))
