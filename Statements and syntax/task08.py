# 8. Write a Python program to remove blank elements from a given array.

arr = ["Red", "Green", "", "Blue", "White"]
arr_new = list(filter(None, arr))

print('Original array:')
print(arr)
print('Remove a blank element from the above array:')
print(arr_new)

# чому не спрацьовувала така дія?
# n = arr.index("")
# arr_new = arr.pop(n)

# що це функція?
# arr2 = ' '.join(arr).split()
# print(arr2)
# .split(), .join(), and list().
# s = ['Hello world']
# s.split() -> ['Hello', 'world"] - from single string make a  list of strings where each string corresponds to a word
# s = ['old 1']
# s.list() -> ['o', 'l', 'd', ' ', '1']  -The list() function turns a string into a list of individual letters
# s = ['a', 'b']
# '-'.join() -> ['a-b']  - 'x'.join(y) joins every element in the list y separated by 'x'
