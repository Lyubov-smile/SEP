# 17. Write a Python program to get the number of even integers in a given array.

arr = [11, 42, 23, 15, 34, 32]

n = 0
for i in range(len(arr)):
    if arr[i] %2 == 0:
        n += 1

print('The number of even integers in a given array is' , n)

