# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.

arr = [1, 2, 3, 5, 4, 3]
if arr.count(3)  == 2 or arr.count(5) == 2:
    print('Array of integers contains 3 or 5 twice')

