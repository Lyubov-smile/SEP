# 8. Write a Python program to remove blank elements from a given array.

arr = ["Red", "Green", "", "Blue", "White"]
print('Original array:')
print(arr)
arr_new = list(filter(None, arr))
print('Remove a blank element from the above array:')
print(arr_new)
n = arr.index("")
arr_2 = arr.copy()
arr_2.pop(n)
print(arr_2)


# work!
# n = arr.index("")
# arr_new = arr.copy()
# arr_new.pop(n)
#print(arr_new)

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
