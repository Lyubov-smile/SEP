# 14. Write a Python program to create a new string from a given string where the first
# and last characters have been exchanged.

a = str("Python")
b = str("Java")
an = a[-1] + a[1:-1] + a[0]
bn = b[-1] + b[1:-1] + b[0]
print(a)
print(an)
print(b)
print(bn)
