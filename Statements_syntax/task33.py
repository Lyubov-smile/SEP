# 33. Write a Python program to sort an given array of strings by length. 

arr = ["abcde", "abdf", "adeab", "abdgeee", "bdefa", "abc", "ab", "a", "bacdef"]

print("Original array: ")
print(arr)
print("Sorted array of strings by length:")
print(sorted(arr, key=len))
