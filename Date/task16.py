a = int(input())
b = int(input())
c = int(input())

if b > a:
    if c > b:
        print('c =', c, 'is greatest')
    else:
        print('b =', b, 'is greatest')
else:
    if c > a:
        print('c =', c, 'is greatest')
    else:
        print('a =', a, 'is greatest')


#a = int(input("Input number 1:"))
#b = int(input("Input number 2:"))
#c = int(input("Input number 3:"))
#if a > b and a > c:
#  print("Max number is 1st = "+str(a))
#elif b > c and b > a:
#  print("Max number is 2nd = "+str(b))
#else:
#  print("Max number is 3rd = "+str(c))
