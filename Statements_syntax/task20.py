# 20. Write a Python program to compute the sum of the numbers of a given array except for the number 17
# and numbers that come immediately after a 17.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

n = arr.index(17)

arr.pop(n)
arr.pop(n)

s = sum(arr)
print(arr)

print('The sum is', s)
