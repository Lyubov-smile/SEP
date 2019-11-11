# 25. Write a Python program to check whether a given array of integers contains two 6's next to each other,
# or there are two 6's separated by one element, such as [6, 2, 6].

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

#arr = [3, 1, 4, 6, 3, 6, 2, 7, 5]

v3 = 0
v5 = 0

for i in range(len(arr)-1):
    if arr[i] == 6 and arr[i+1] == 6:
        v3 = 1
for i in range(len(arr)-2):
    if arr[i] == 6 and arr[i+2] == 6 and  arr[i+1] != 6:
            v5 = 1


if v3:
    print("A given array of integers contains two 6's next to each other")
elif v5:
    print("A given array of integers contains  two 6's separated by one element")
else:
    print('false')