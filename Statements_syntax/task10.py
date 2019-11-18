# 10. Write a Python program to create an array with the elements "rotated left" of a given array of ints length 3.
#Sample Output:
#[2, 5, 1]
#[2, 3, 1]
#[2, 4, 1]

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

a1 = arr.copy()
a2 = a1[1:-1]
a2.reverse()
a1[1:-1] = a2
print(a1)
