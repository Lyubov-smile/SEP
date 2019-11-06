# 21. Write a Python program to compute the sum of every third element of a given array of integers.

arr = [11, 42, 23, 17, 15, 34, 32, 28, 43, 51]

s = 0
i = 0
while i <= len(arr):
    s += arr[i]
    i += 3

print('The sum of every third element of a given array is', s)
