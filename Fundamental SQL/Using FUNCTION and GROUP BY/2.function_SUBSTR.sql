select StudentID, substr(FirstName,2,3) as Initial from students;
# Mengekstrak karakter/string yang diinginkan
#   contoh: substr('Alphabet', 3, 2) = 'ph'
