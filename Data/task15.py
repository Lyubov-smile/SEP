# 15. Write a Python program to check two integers and return true if one of them is 20 otherwise return their sum.  

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))
if (a == 20) or (b == 20):
    print('True')
else:
    print(a+b)
