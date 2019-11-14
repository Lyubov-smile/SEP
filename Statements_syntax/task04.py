# 4  Write a Python program to check whether first and the last element are the same as a given array of integers.
# The array length must be 1 or more.

import random

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

if len(arr) < 1:
    print("Array must include more then 0 elements!")

if arr[0] == arr[-1]:
    print('True')
else:
    print('False')

