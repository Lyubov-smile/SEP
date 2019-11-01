s = str(input("Insert a list: "))
n = int(input("Insert a number: "))
if len(s) >= 3 :
    sn = s[0:3]*n
else:
    sn = s * n
print(sn)

