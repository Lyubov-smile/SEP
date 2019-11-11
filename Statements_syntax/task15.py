# 15. Write a Python program to find the largest odd value from a given array.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

arr_odd = []
for i in range(len(arr)):
    if arr[i] %2 == 1:
        arr_odd.append(arr[i])

print(max(arr_odd))
