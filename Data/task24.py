# 24. Write a Python program to print the elements of a given array.  Sample array : ["Ruby", 2.3, Time.now] 

import sys
sv = (sys.version)
sv1 = sv[0:6]
print(sv)
print(sv1,"\n")



import datetime
import array
now = datetime.datetime.now()
dt = datetime.datetime.now().strftime("%H.%M")
print(dt, type(dt))
dt1 = float(dt)
a1 = "Ruby"
a2 = 2.3
a3 = dt1
print(a1, a2, a3)
ar = [a1, a2, a3]
print(ar)

#ar = ar + [dt]
#a = ["Ruby", 2.3, % now.hour, % now.minute"] 
#print(a[0],a[1],a[2])




