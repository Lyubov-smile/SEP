# 15. Write a Python program to find the largest odd value from a given array.

arr = [1, 2, 3, 5, 4, 3]

arr_odd = []
for i in range(len(arr)):
    if arr[i] %2 == 1:
        arr_odd.append(arr[i])

print(max(arr_odd))
