# 38. Given the single-mass array with predefined values with a size of 10 items.
# Show on the screen array, and find the values that are repeated two and more times.

arr = [2, 3, 4, 2, 4, 5, 4, 7, 8, 9]
arr2 = list(set(arr))
print(arr)
print()
for j in range(len(arr2)):
    s = 0
    for i in range(len(arr)):
        if arr[i] == arr2[j]:
            s += 1
        if i == len(arr) - 1:
            if s > 1:
                print(arr2[j], "happened", s, "times in array")
