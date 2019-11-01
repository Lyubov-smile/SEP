s = int(input('Input distance between cities: '))
vr = int(input('Input speed of a rabbit: '))
vt= int(input('Input speed of a turtle: '))

t = s / (vt + vr)
sb = vt * t
print(sb)
