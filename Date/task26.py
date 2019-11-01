subject_marks = {"Literature": 74, "Science": 89, "Math": 91}

def Sum(myDict):
    s = 0
    for i in myDict:
        s = s + myDict[i]
    return s

print('Total Marks: ', Sum(subject_marks))


#def returnSum(dict):
#    sum = 0
#    for i in dict.values():
#        sum = sum + i
#    return sum
#print("Sum :", returnSum(subject_marks))
