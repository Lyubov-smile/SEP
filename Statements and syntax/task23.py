# 23. Write a Python program to check whether a given value appears everywhere in a given array.
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.

arr = [1, 3, 5, 2, 7, 5]

value = 3
for i in range(len(arr)):
    if arr[i] == 3:
        i += 1
        inf = 'Every element in array = 3'
    else:
        inf = 'Not every element in array = 3'
        break

print(inf)

