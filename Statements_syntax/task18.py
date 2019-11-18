# 18. Write a Python program to find the difference between the largest and smallest values of a given array of integers.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

arr_max = max(arr)
arr_min = min(arr)
n = arr_max - arr_min
print('The difference between the largest and smallest values of a given array of integers is', n)

