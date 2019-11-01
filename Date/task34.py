myl = [1, 5, 7, 8, 1, 5, 6, 7, 3, 4]

from collections import Counter

x = 5
d = Counter(myl)

print(d[x])

#print('{} has occured {} times'.format(x, d[x]))