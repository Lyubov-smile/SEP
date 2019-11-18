# 20. Write a Python program to compute the sum of the numbers of a given array except for the number 17
# and numbers that come immediately after a 17.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

n = arr.index(17)

arr.pop(n)
arr.pop(n)

s = sum(arr)
print(arr)

print('The sum is', s)






# arr [1, 2, 17, 3, 4, 17, 5, 6] it doesn't work
arr_new = arr.copy()
for i in range(n):
    ni = arr_new.index(17)
    if i == ni:
        arr_new.pop(i)
        arr_new.pop(i)
        i += 2
        ni = arr_new.index(17)


print('The sum is', sum(arr_new))
