# 26. Write a Python program to check whether there is a 2 in the array with a 3 somewhere later in a given array of integers.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

#arr = [3, 1, 4, 6, 2, 3, 6, 2, 7, 5]

v2 = 0
v3 = 0

for i in range(len(arr)):
    if arr[i] == 2:
        v2 = 1
        for j in range(i+1, len(arr)):
            if arr[j] == 3:
                v3 = 1
                break


if v2 and v3:
    print("True")
else:
    print('false')
