# 17. Write a Python program to check if a number is within 10 of 100 or 200. (E.g. 90, 110, 190, 210) 

a = int(input('Input number: '))

if abs(100 - a) <= 10 or abs(200 - a) <= 10:
   print("Number is within 10 of 100 or 200")
else:
   print("Number isn't within 10 of 100 or 200")


#a = int(input())
#def near_hundred(n):
#    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
#        return True
#    else:
#        return False
#print(near_hundred(a))

