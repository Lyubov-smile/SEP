# 13. Write a Python program which accepts the radius of the sphere as input and compute the volume.

r = float(input('Input the radius of the circle: '))

import math

v = r**3*math.pi
print('The volume of the sphere is:', v)
