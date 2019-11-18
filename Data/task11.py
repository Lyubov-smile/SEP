# 11. Write a Python program to create a new string where "if" is added to the front of a given string.
# If the string already begins with "if", return the string unchanged.

s = str(input('Insert the string: '))
if s[0:2] == 'if':
    sn = s
    print(sn)
else:
    sn = 'if' + s
    print(sn)
