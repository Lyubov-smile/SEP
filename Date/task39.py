a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if a % 5 != b % 5:
    if a > b:
        print(a)
    else:
        print(b)
else:
    if a < b:
        print(a)
    elif b < a:
        print(b)
    else:
        print(0)

