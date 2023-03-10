select StudentID, substring_index(Email, '@', 1) as Name from students;
