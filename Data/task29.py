# 29. Write a Python program to check whether a string 'Java' appears at index 1 in a given sting,
# if 'Java' appears return the string without 'Java' otherwise return the string unchanged.  

s = str(input('Input string: '))
if s[0:4] == 'Java':
    s = s[4:]
print(s)