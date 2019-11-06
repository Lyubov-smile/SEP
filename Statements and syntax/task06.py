# 6. Write a Python program to remove duplicate elements from a given array.

arr = [1, 2, 3, 4, 1, 2, 2, 3, 5, 6]
arr_new = list(set(arr))
# set don't include duplicate elements
# or another one
#arr_new = []
#for i in arr:
#    if i not in arr_new:
#        arr_new.append(i)
print('Original array:')
print(arr)
print('Array with unique elements:')
print(arr_new)

