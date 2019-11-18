# 23. Write a Python program to check whether a given value appears everywhere in a given array.
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

#arr = [1, 3, 5, 2, 7, 5]

value = int(input('Input value which you want to check:'))
for i in range(len(arr)):
    if arr[i] == value:
        i += 1
        inf = 'Every element in array = '
    else:
        inf = 'Not every element in array = '
        break

print(inf, value)

