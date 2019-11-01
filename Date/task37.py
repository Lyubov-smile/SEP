a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if a == 11 or b == 11:
    print(11)
elif a + b == 11:
    print(11)
elif a - b == 11 or b - a == 11:
    print(11)
else:
    print('none')
