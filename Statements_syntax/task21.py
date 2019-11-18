# 21. Write a Python program to compute the sum of every third element of a given array of integers.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

s = 0
i = 0
while i <= len(arr):
    s += arr[i]
    i += 3

print('The sum of every third element of a given array is', s)
