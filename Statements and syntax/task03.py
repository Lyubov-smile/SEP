# 3 Write a Python program to pick a number of random elements from a given array.
import random
arr = [12, 34, 23, 56]
print('2 random elements from the array.')
print(random.sample(arr, 2))
print('3 random elements from the array.')
print(random.sample(arr, 3))

#print('2 random elements from the array.')
#print(random.choices(arr, k=2))
#print('3 random elements from the array.')
#print(random.choices(arr, k=3))
#random.shuffle() -> mix the list