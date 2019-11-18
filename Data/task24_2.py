# 24. Write a Python program to print the elements of a given array.  Sample array : ["Ruby", 2.3, Time.now] 

import datetime

arr = []
arr.append("Ruby")
arr.append(2.3)
arr.append(float(datetime.datetime.now().strftime("%H.%M")))
print (arr)
for i in range(len(arr)):
    print(arr[i])
#or

a = ["Ruby", 2.3, str(datetime.datetime.now().strftime("%H:%M"))]
for i in range(len(a)):
    print(a[i])






