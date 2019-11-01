a = int(input())
b = int(input())
c = int(input())

print('All three')

if not((1 <= a <= 10) and (1 <= b <= 10) and (1 <= c <= 10)):
    print('true')
else:
    print('False')

print('Only one of them')
if not(((1 <= a <= 10) and (1 <= b <= 10)) or ((1 <= b <= 10) and (1 <= c <= 10)) or ((1 <= a <= 10) and (1 <= c <= 10))):
    print('true')
else:
    print('False')
