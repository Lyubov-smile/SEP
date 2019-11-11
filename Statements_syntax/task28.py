# 28. Write a Python program to find most occurred item in a given array.

import collections

arr = [10, 20, 30, 40, 10, 10, 20]
counter = collections.Counter(arr)
print(counter)



