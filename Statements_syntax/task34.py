# 34. Compress the array, and removing all 0 from it and fill in the elements freed on the right side with the values ​​-1

# if only remove
arr = [10, 20, 0, 30, 40, 20, 30, 0, 40, 20, 0, 70, 20]
arr2 = [x for x in arr if x != 0]
print(arr2)

# if add -1
arr3 = []
for i in range(0, len(arr)):
    if arr[i] != 0:
        arr3.append(arr[i])
    else:
        arr3.append(-1)
print(arr3)
