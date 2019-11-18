# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.

subject_marks = {"Literature": 74, "Science": 89, "Math": 91}

def returnSum(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum
print("Sum :", returnSum(subject_marks))

myl2 = ['a', 'd', 'r', 'a', 'd', 'w', 'a', 't', 'r', 'a']
myl3 = myl2.count('a')
print(myl3)