
arr = [1, 2, 3]
max = arr[0]
if arr[-1] > max:
    max = arr[-1]

for i in range(len(arr)):
    arr[i] = max

print(arr)
