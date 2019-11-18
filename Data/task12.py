# 12. Write a Python program to create a new string from a given string using the first three characters
# or whatever is there if the string is less than length 3. Return n copies of the string.

s = str(input("Insert a list: "))
n = int(input("Insert a number: "))
if len(s) >= 3:
    sn = s[0:3]*n
else:
    sn = s * n
print(sn)

