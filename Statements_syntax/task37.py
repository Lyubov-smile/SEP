#

n = int(input('Input size of array: '))
m = int(input('Input size of array: '))

arr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        r = int(input("Insert element: "))
        arr[i].append(r)



print(arr)

arr2 = [[] for i in range(n)]
for i in range(n):
    for j in range(m):
        r = int(input("Insert element: "))
        arr2[i].append(r)

print(arr2)