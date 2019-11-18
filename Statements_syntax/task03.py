# 3 Write a Python program to pick a number of random elements from a given array.

import random

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

print('2 random elements from the array.')
print(random.sample(arr, 2))
print('3 random elements from the array.')
print(random.sample(arr, 3))

#print('2 random elements from the array.')
#print(random.choices(arr, k=2))
#print('3 random elements from the array.')
#print(random.choices(arr, k=3))
#random.shuffle() -> mix the list
