# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

if arr.count(3) == 2 or arr.count(5) == 2:
    print('Array of integers contains 3 or 5 twice')

