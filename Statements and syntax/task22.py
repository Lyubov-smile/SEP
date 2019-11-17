# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.

arr = [3, 5, 3, 5, 3]
#[1, 3, 5, 2, 7, 5]


for i in range(len(arr)):
    if arr[i] == 3 or arr[i] == 5:
        i += 1
        inf = 'Every element in array = 3 or 5'
    else:
        inf = 'Not every element in array = 3 or 5'
        break

print(inf)