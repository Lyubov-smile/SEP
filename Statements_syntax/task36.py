# 36. Write a program where a need to counts the number of times a number appear in an array.

n = int(input('Input the length of your array: '))
if n < 1:
    print("The length of array can't be less than 1!")

arr = []
for i in range(n):
    arr.append(int(input('Input an integer element of array: ')))

num = int(input('Input a number which you want to check in array: '))

qty = arr.count(num)
print(num,'meets in array', qty, 'times')