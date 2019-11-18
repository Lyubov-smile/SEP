# 36. Write a Python program to check if the sequence of numbers 10, 20, 30 appears anywhere in a given array of integers.  

a = [10, 20, 30, 10, 40, 10]
a2 = [10, 30, 10, 20, 10]
a3 = [40, 10, 20, 30, 10, 20, 10]
a4 = [10, 30, 10, 20, 30, 50]

b = [10, 20, 30]
a = a
i = 0
while i < len(a)-2:
    if b == a[i:i+3]:
        print('True')
        break
    else:
        i = i + 1
else:
    print('False')


