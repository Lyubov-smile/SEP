# 16. Write a Python program to create a new array using the first three elements of a given array of integers.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

arr_new = arr[0:3]

print(arr_new)