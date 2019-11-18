# 35. Convert the array so that the first go all negative elements, and then positive (0 is considered positive)

arr = [1, 4, 5, -2, 3, -7, 0, -4]
print(arr)
print(sorted(arr))

# цей спосіб змінює оригінальний масив, або потрібно створити копію даного масиву і змінювати її arr.copy()
# arr.sort()
# print(arr)