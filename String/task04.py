# 4 Створити функцію, що дозволяє вставляти (видаляти) стрічку в (з) масив (-а) стрічок.


def add_string(array, string, position):
    if position > len(array):
        array.append(string)
    else:
        array.insert(position-1, string)
    return array


def del_string(array, string, qty):
    for i in range(0, qty):
        if string in array:
            array.remove(string)
    return array


def change_array(action):
    if action == 'add':
        function = add_string(array, string, position)
    elif action == 'del':
        function = del_string(array, string, qty)
    else:
        print("Incorrect action command")
    return function


array = ['abd', 'qty', 'sdr', 'qty', 'dfg', 'rgh', 'rfh', 'qty']
string = 'qty'
action = str(input('Input add or del: '))
if action == 'add':
    position = int(input('Input position of adding: '))
elif action == 'del':
    qty = input('Input how mach strings you want ot delete: ')
    if qty == 'all':
        qty = len(array)
    else:
        qty = int(qty)


print(change_array(action))

