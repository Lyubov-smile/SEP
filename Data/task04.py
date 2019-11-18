# 4. Write a Python program which accepts the radius of a circle from the user and compute the parameter and area.

r = float(input('Input the radius of a circle: '))
import math

p = 2 * r * math.pi
s = r ** 2 * math.pi
print('P=', p, sep='')
print('S=', s, sep='')
