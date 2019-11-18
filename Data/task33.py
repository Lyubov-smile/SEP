# 33. Write a Python program to check two positive integer values and return the larger value that is in the range
# 20..30 inclusive, or return 0 if no number is in that range. 

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if 20 <= a <= 30 and 20 <= b <= 30 and a > b:
    print(a)
elif 20 <= a <= 30 and 20 <= b <= 30 and a < b:
    print(b)
#elif 20 <= a <= 30 and not(20 <= b <= 30):
#    print(a)
#elif not(20 <= a <= 30) and 20 <= b <= 30:
#    print(b)
else:
    print(0)


#if 20 <= a <= 30:
#    if 20 <= b <= 30:
#        if a > b:
#            print(a)
#        if a < b:
#            print(b)
#    else:
#        print(a)
#elif 20 <= b <= 30:
#    print(b)
#else:
#    print(0)