# 24. Write a Python program to check whether a given array contains a 3 next to a 3 or a 5 next to a 5, but not both.

arr = [3, 1, 4, 2, 7, 5]

v3 = 0
v5 = 0

for i in range(len(arr)-1):
    if arr[i] == 3 and arr[i+1] == 3:
        v3 = 1
        print(v3)
    if arr[i] == 5 and arr[i+1] == 5:
        v5 = 1
        print(v5)

if v3 and v5:
    print('false')
elif v3 or v5:
    print('true')
else:
    print('false')