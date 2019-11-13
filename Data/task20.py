# 20. Write a Python program to create a new string from a given string with the last character added
# at the front and back of the given string. The length of the given string must be 1 or more.

a = str(input("Input string value: "))
b = a[-1]+a+a[-1]
print(b)