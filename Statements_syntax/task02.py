# 2 Write a Python program to check whether 7 appears as either the first or last element in a given array.
# The array length must be 1 or more.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))
ni = int(input('Input an integer number which you want to check in array: '))
if arr[0] == ni or arr[-1] == ni:
    #    print(ni, 'is the first or last element in a given array.')
    print('True')
else:
    #    print(ni, 'isn\'t the first and last element in a given array.')
    print('False')

