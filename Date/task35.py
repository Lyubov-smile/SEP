#25. Write a Python program to check two non-negative integer values and return true if they have the same last digit.
#35. Write a Python program to check two non-negative integer values and return true if they have the same last digit. 
#25 and 35 are the same

a = int(input('Insert non-negative integer value 1: '))
b = int(input('Insert non-negative integer value 2: '))
if a > 0 and b > 0 and a %10 == b %10 :
    print('True')
else:
    print('False')