select StudentID, FirstName, LastName, ceiling(Semester1) as Semester1, ceiling(Semester2) as Semester2, MarkGrowth from students;
# Mengembalikan nilai integer terbesar yang terdekat dengan nilai input 
#   contoh: ceiling(17.34) = 17, ceiling(-95.34) = -95
