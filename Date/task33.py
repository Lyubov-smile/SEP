a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if 20 <= a <= 30 and 20 <= b <= 30 and a > b:
    print(a)
elif 20 <= a <= 30 and 20 <= b <= 30 and a < b:
    print(b)
else:
    print(0)
