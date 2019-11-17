# 2 Write a Python program to check whether 7 appears as either the first or last element in a given array.
# The array length must be 1 or more.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less then 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an number element of array: ')))

if arr[0] == 7 or arr[-1] == 7:
#    print('7 is the first or last element in a given array.')
    print('True')
else:
#    print('7 isn\'t the first and last element in a given array.')
    print('False')

