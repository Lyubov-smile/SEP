# 9. Write a Python program to check three numbers and return true if one or the other is small, but not both.
# A number is called "small" if it is in the range 1..10 inclusive.  

a = int(input())
b = int(input())
c = int(input())

print('Not all three')
if not((1 <= a <= 10) and (1 <= b <= 10) and (1 <= c <= 10)):
    print('true')
else:
    print('False')

print('Only one of them')
if not(((1 <= a <= 10) and (1 <= b <= 10)) or ((1 <= b <= 10) and (1 <= c <= 10)) or ((1 <= a <= 10) and (1 <= c <= 10))):
    print('true')
else:
    print('False')
