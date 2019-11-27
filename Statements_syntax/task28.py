# 28. Write a Python program to find most occurred item in a given array.

import collections

arr = [10, 20, 30, 40, 10, 10, 20]
counter = collections.Counter(arr)
print(counter)

print('{', end='')
for k, v in counter.items():
    print(k, '=>', v, sep='',  end=(', ' if k < max(arr) else '}\n'))

#properties of the print(), sep from separator



