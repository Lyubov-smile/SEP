# 8. Write a Python program to check three numbers and return true if one or more of them are small.
# A number is called "small" if it is in the range 1..10 inclusive. 

a = int(input())
b = int(input())
c = int(input())
if 1 <= a <= 10:
    print('true')
elif 1 <= b <= 10:
    print('true')
elif 1 <= c <= 10:
    print('true')
else:
    print('False')

# or it can be written like this
# if (1 <= a <= 10) or (1 <= b <= 10) or (1 <= c <= 10):
#     print('true')
# else:
#     print('False')

# print(bool((1 <= a <= 10) or (1 <= b <= 10) or (1 <= c <= 10)))

#   written from commit
#if a in range(1,11):
#    print('true')
#elif b in range(1,11):
#    print('true')
#elif c in range(1,11):
#    print('true')
#else:
#    print('False')
