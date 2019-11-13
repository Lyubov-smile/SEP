# 31. Write a Python program to check two integers and return whichever value is nearest to the value 10,
# or return 0 if two integers are equal.  

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if a == b:
    print(0)
elif abs(a - 10) < abs(b - 10):
    print(a)
else:
    print(b)
