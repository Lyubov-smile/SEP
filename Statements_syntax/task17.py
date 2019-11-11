# 17. Write a Python program to get the number of even integers in a given array.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

n = 0
for i in range(len(arr)):
    if arr[i] %2 == 0:
        n += 1

print('The number of even integers in a given array is', n)

