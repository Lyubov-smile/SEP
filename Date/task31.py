a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if a == b:
    print(0)
elif abs(a - 10) < abs(b - 10):
    print(a)
else:
    print(b)
