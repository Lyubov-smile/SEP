# # 32. Write a Python program to check two integer values and return true if they are both in the range
# 10..20 inclusive, or they are both in the range 20..30 inclusive.  

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if (10 <= a <= 20 and 10 <= b <= 20) or (20 <= a <= 30 and 20 <= b <= 30):
    print('True')
else:
    print('False')
