# 37. In a two-dimensional array of order M and N, swap the specified columns.

row = int(input('Enter the number of rows: '))
col = int(input('Enter the number of columns: '))

arr = []
for i in range(row):
    arr.append([])
    for j in range(col):
        el = int(input("Insert element: "))
        arr[i].append(el)

n = int(input('Input the first value of row between o and '+str(col)+': '))
m = int(input('Input the second value of row between o and '+str(col)+': '))

print('The two-dimensional array of order '+str(row)+' and '+str(col)+' is: ')
for i in arr:
    print(i)

arr_new = arr.copy()

for i in range(row):
    temp = arr_new[i][n]
    arr_new[i][n] = arr_new[i][m]
    arr_new[i][m] = temp

print('The array with changed columns is: ')
for i in arr_new:
    print(i)
