
import os
# filename - task06.py
Filename = str(input('Print the file name in format *.py: '))
p = os.path.abspath(Filename)
p2 = os.path.splitext(Filename)
p3 = os.path.dirname(p)

print('Filename: ', Filename)
print('Base name: ', p2[0])
print('Extension: ', p2[-1])
print('Pathname: ', p3)

