# 30. Write a Python program to create a string using the first two characters (if present) of a given string
# if the first character is 'p' and second one is 's' otherwise return a blank string.

s = str(input('Input string: '))
if s[0:2] == 'ps':
    sn = 'ps'
else:
    sn =""
print(sn)
