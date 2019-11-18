# 11. Write a Python program to create a new array with the elements in reverse order from a given an array of integers length 3. 

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

a1 = arr.copy()
a1.reverse()
print(a1)

#a2= list(reversed(arr))
#print(a2)
