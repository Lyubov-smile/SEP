# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values.

arr = [11, 42, 23, 15, 34, 32]

arr_max = max(arr)
arr_min = min(arr)
arr_new = arr.copy()

arr_new.remove(arr_max)
arr_new.remove(arr_min)

ave = sum(arr_new)/ len(arr_new)

print('The average values of a given array of except the largest and smallest valuess is' , ave)

