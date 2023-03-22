# Fitur .split()
#   Memecah sebuah string berdasarkan string lainnya ke dalam sebuah list.
print(">>> Fitur .split()")
frasa = "ani dan budi dan wati dan johan"
karakter = frasa.split("dan")
print(karakter)
kata = frasa.split(" ")
print(kata)
# Fitur .join()
#   Menggabungkan sebuah list yang berisikan string 
#   berdasarkan sebuah string yang telah didefinisikan.
print(">>> Fitur .join()")
pemisah = " dan "
karakter = ["Ricky", "Peter", "Jordan"]
frasa = pemisah.join(karakter)
print(frasa)
frasa = " ".join(karakter)
print(frasa)
# Fitur .replace()
#   Menggantikan kemunculan suatu string 
#   tertentu dengan string lainnya dalam sebuah string.
print(">>> Fitur .replace()")
frasa = "apel malang apel yang paling segar, apel sehat, apel nikmat"
frasa = frasa.replace("apel", "jeruk")
print(frasa)
