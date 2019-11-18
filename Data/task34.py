# 34. Write a Python program to count the number of 5's in a given array.  

myl = [1, 5, 7, 8, 1, 5, 6, 7, 3, 4]

from collections import Counter

x = 5
d = Counter(myl)

print(d[x], "\n")

#print('{} has occured {} times'.format(x, d[x]))

print(myl.count(5))

#myl2 = ['a', 'd', 'r', 'a', 'd', 'w', 'a', 't', 'r', 'a']
#print("\n", myl2.count('a'))