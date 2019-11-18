# 5 Write a Python program to compute the sum of elements in a given array.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

print('Original array:', arr)

print('Sum of the values of the above array:', sum(arr))

