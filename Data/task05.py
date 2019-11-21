# 5. Write a Python program to check if a string starts with "if".

s = str(input('Input a string: '))
print(s[0:2] == 'if')

#if bool(s[0:2] == 'if'):
#    print('The string starts with "if".')
#else:
#    print('The string doesn\'t starts with "if".')

#   written from commit
result = s.startswith('if')
print(result)
