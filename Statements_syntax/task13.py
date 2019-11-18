# 13. Write a Python program to concatenate an array of arrays into one.

n1 = int(input('Input the length of your 1st array: '))
if n1 < 1:
    print("The length of array can't be less than 1!")
a1 = []
for i in range(n1):
    a1.append(int(input('Input a number element of array: ')))

n2 = int(input('Input the length of your 2nd array: '))
if n2 < 1:
    print("The length of array can't be less than 1!")
a2 = []
for i in range(n2):
    a2.append(int(input('Input a number element of array: ')))

a3 = a1 + a2
print(a3)
#a1.extend(a2)
#print(a1)
