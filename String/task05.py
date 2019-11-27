# 5. Створити функцію для перевірки коректності розстановки дужок у виразі.

string = str(input('Input your expression: '))


def brackets_qty(s):
    count1 = 0 # ()
    count2 = 0 # {}
    count3 = 0 # []
    for i in range(len(string)):
        if string[i] == '(':
            count1 += 1
        elif string[i] == ')':
            count1 -= 1
        elif string[i] == '[':
            count2 += 1
        elif string[i] == ']':
            count2 -= 1
        elif string[i] == '{':
            count3 += 1
        elif string[i] == '}':
            count3 -= 1
        if count1 < 0 or count2 < 0 or count3 < 0:
            print('check brackets')
            break
    if count1 == count2 == count3 == 0:
        message = 'Correct placement of the brackets in the expression.'
    else:
        message = 'Incorrect placement of the brackets in the expression. Missed some brackets!'
    return(message)


print(brackets_qty(string))

