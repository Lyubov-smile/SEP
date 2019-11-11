# 27. Write a Python program to convert an array into an index hash. 

arr = [10, 20, 30, 40]
d = dict.fromkeys(arr, 'nil')

print('Original array:')
print(arr)
print('Index Hash:')
print(d)