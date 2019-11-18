# 31. Write a Python program to iterate an array starting from the last element. 

arr = [10, 20, 30, 40, 10, 10, 20]

print('Original array:')
print(arr)
print("Reverse array:")

for i in range(len(arr), 0, -1):
    print (arr[i-1])

# цей метод міняє оригінальний список
#arr.reverse()
#for i in range(len(arr)):
#    print(arr[i])


# цей метод витягує поелементно в зворотному порядку не змінюючи оригінальний список
# array=[0,10,20,40]
#for i in reversed(array):
#    print(i)

# цей метод створює копію нашого списку
#arev = list(reversed(array))
#for i in range(len(arev)):
#    print(arev[i])

# цей метод створює копію нашого списку у зворотному порядку
#L = [0,10,20,40]
#L_rev = L[::-1]
#print(L[::-1])
#print(L_rev)
