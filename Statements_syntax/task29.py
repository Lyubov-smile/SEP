# 29. Write a Python program to check whether all items are identical in a given array. 
# [10, 20, 30, 40, 10, 10, 20]
# [10, 10, 10]

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))


mes = "false"
for i in range(1, len(arr)):
    if arr[i] == arr[0]:
        mes = "true"
    else:
        break

print('Original array:')
print(arr)
print('Is all items are identical?')
print(mes)