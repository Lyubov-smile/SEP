# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))
#arr = [1, 3, 5, 2, 7, 5]


for i in range(len(arr)):
    if arr[i] == 3 or arr[i] == 5:
        i += 1
        inf = 'Every element in array = 3 or 5'
    else:
        inf = 'Not every element in array = 3 or 5'
        break

print(inf)