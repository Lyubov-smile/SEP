# 37. Write a Python program to check two given integers and return 11 if either one is 11.
# Return their sum or difference if sum or difference is 11. 

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))
n = 11
if a == n or b == n:
    print(n)
elif a + b == n:
    print(n)
elif a - b == n or b - a == n:
    print(n)
else:
    print('none')
