# 12. Write a Python program to find the larger between the first and last elements of a given array of integers and length 3.
# Replace all the other values to be that value. Return the changed array. 


arr = [1, 2, 3]
max = arr[0]
if arr[-1] > max:
    max = arr[-1]

for i in range(len(arr)):
    arr[i] = max

print(arr)
