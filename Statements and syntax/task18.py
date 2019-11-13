# 18. Write a Python program to find the difference between the largest and smallest values of a given array of integers.

arr = [11, 42, 23, 15, 34, 32]

arr_max = max(arr)
arr_min = min(arr)
n = arr_max - arr_min
print('The difference between the largest and smallest values of a given array of integers is', n)

