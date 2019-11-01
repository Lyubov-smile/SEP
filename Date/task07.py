import re
import os
Filename = str(input('Print the file name in format *.py: '))


print('Filename: ', Filename)
print('Base name: ', Filename)
print('Extension: ', Filename)
print('Pathname: ', Filename)

#Filename: task06.py
#Base name: task06
#Extension: .py
#Pathname: /user/system

#import os
p = os.path.abspath(Filename)
print(p)

#import re

#Filename = str(input('Print the file name: '))

name1= re.split(r'/.', Filename)
print (name1)
print ('Filename: ',Filename)
print ('Base name: ',name1[0])
print ('Extension: ','.'+ name1[-1])
print ('Pathname: ','')

#import os
p = os.path.abspath(Filename)
pp = os.path.dirname(Filename)
print(p)
print(pp)
