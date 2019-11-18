# 7. Write a Python program to check two given arrays of integers and test if they have the same first element
# or they have the same last element. Both arrays length must be 1 or more.  

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

if a1[0] == a2[0] or a1[-1] == a2[-1]:
    print('True')
else:
    print('False')