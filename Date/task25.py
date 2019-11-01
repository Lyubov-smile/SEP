a = int(input('Insert non-negative integer value 1: '))
b = int(input('Insert non-negative integer value 2: '))
if a > 0 and b > 0 and a %10 == b %10 :
    print('True')
else:
    print('False')