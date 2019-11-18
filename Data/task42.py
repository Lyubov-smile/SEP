# 42. На зустріч один одному відповідно з міста А та міста Б рухається заєць та черепаха. Ввести з клавіатури відстань
# між містами, швидкість зайця та швидкість черепахи. Обчислити на якій відстані від міста Б вони зустрінуться.

s = int(input('Input distance between cities: '))
vr = int(input('Input speed of a rabbit: '))
vt = int(input('Input speed of a turtle: '))

t = s / (vt + vr)
sb = vt * t
print(sb)
