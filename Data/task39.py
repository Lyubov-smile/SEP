# 39. Write a Python program to check two given integers and return the larger value. However, if the two values
# have the same remainder when divided by 5 then return the smaller value and if the two values are the same, return 0. 

a = int(input('Input integer number: '))
b = int(input('Input integer number: '))

if a == b:
    print(0)
elif a % 5 != b % 5:
    if a > b:
        print(a)
    else:
        print(b)
else:
    if a < b:
        print(a)
    elif b < a:
        print(b)

