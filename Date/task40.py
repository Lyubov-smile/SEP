a = int(input('Input integer number in the range 10..99: '))
b = int(input('Input integer number in the range 10..99: '))

a1 = a % 10
a2 = a // 10
b1 = b % 10
b2 = b // 10

if a1 == b1 or a1 == b2:
    print('True')
elif a2 == b1 or a2 == b2:
    print('True')
else:
    print('False')

