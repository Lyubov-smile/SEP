# 39. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the value that is the smallest nonpaired number.

print('Input array 10 length')
arr = []
for i in range(10):
    arr.append(int(input('Input next value: ')))

print(arr)
arr_1 =[]
for i in range(10):
    if arr[i] %2 == 1:
        arr_1.append(arr[i])
print('The smallest nonpaired number is', min(arr_1))
