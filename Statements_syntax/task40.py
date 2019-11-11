# 40. Given the single-mass array. Cyclically shift the array on the K elements, on the right or left side.

n = int(input('Input the length of array: '))
arr = []
for i in range(n):
    arr.append(int(input('Input next value: ')))

k = int(input('Input the number: '))
m = str(input('Input the direction: l/r: '))


arr_new = []

for i in range(n):
    if m == 'r':
        arr_new = arr[-k:] + arr[0:-k]
    if m == 'l':
        arr_new = arr[k:] + arr[0:k]

print(arr)
print(arr_new)

