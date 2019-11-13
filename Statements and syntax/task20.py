# 20. Write a Python program to compute the sum of the numbers of a given array except for the number 17
# and numbers that come immediately after a 17.

arr = [11, 42, 23, 17, 15, 34, 32]
n = arr.index(17)

arr.pop(n)
arr.pop(n)

s = sum(arr)
print(arr)

print('The sum is', s)
