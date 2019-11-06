# 4  Write a Python program to check whether first and the last element are the same as a given array of integers.
# The array length must be 1 or more.

arr = [1, 2, 4, 2, 1]
if len(arr) < 1:
    print("Array must include more then 0 elements!")

if arr[0] == arr[-1]:
    print('True')
else:
    print('False')


n = int(input('Input the length of your array: '))
if n < 1:
    print('Length must be more then 0')

arr2 = []
for i in range(n):
    arr2.append(int(input('Input an integer element of array: ')))

if arr2[0] == arr2[-1]:
    print('True')
else:
    print('False')



