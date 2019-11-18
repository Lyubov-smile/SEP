# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

arr_max = max(arr)
arr_min = min(arr)
arr_new = arr.copy()

arr_new.remove(arr_max)
arr_new.remove(arr_min)

ave = sum(arr_new) / len(arr_new)

print('The average values of a given array of except the largest and smallest valuess is', ave)

