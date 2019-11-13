# 3. Write a Python program to create a new string which is n copies of a given string where n is a non-negative integer.

a = str(input('Input a string'))
n = int(input('Input integer number'))
# a=str('a')
# n=int(5)
for i in range(n + 1):
    print(a * i)
