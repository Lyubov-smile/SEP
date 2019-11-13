# 28. Write a Python program to test whether a year is leap year or not.  

year = int(input('Input year: '))
if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
    print(year, 'is leap year')
#if year % 4 != 0 or (year % 4 == 0 and year % 100 == 0 and year % 400 != 0):
else:
    print(year, 'is not leap year')


