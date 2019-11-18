# 9. Write a Python program to split a delimited string into an array.  

st = "Red, Green, Blue, White"
st1 = st.split(',')
sn = "1, 3, 4, 5, 7"
sn1 = sn.split(',')
sn2 = []
for i in range(len(sn1)):
    sn2.append(int(sn1[i]))
print(sn2)
print('Original delimited string:')
print(st1)
print('String to array:')
print(sn1)

# How to make sn1 like a numbers???
