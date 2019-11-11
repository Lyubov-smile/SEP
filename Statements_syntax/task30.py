# 30. Write a Python program to search items start with specified string of a given array.  

#n = int(input('Input the length of your array: '))
#if n < 1:
#    print("The length of array can't be less than 1!")
#
#arr = []
#for i in range(n):
#    arr.append(str(input('Input a string element of array: ')))

arr = ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
a1 = []
a2 = []
for i in range(0, len(arr)):
    if arr[i][0:2] == "ab":
        a1.append(arr[i])
    if arr[i][0] == "b":
        a2.append(arr[i])

print('Original array:')
print(arr)
print("Search items start with 'ab':")
print(a1)
print("Search items start with 'b':")
print(a2)
