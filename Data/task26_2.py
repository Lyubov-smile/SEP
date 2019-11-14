# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.

subject_marks = {"Literature": 74, "Science": 89, "Math": 91}

s = 0
for name, mark in subject_marks.items():
  s += mark

print('Total Marks: ', s)

for n, m in subject_marks.items():
  print(n)
  print(m)

