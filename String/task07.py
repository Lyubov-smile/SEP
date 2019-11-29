# 7 Написати функцію, що перетворює дробове або ціле число в рядок.

# converts a number to a string
num_0_19 = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
            17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
num_20_90 = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
             90: 'ninety'}


def convert_number_string_100(number):
    number_string = ''
    n1 = number // (10 ** 2)
    n2 = number % (10 ** 2)
    if n1 > 0:
        number_string += num_0_19[n1] + ' hundred '
    if n2 < 20:
        number_string += num_0_19[n2]
    elif n2 > 19:
        n1 = n2 % 10
        n2 = n2 - (n2 % 10)
        number_string += num_20_90[n2] + ' ' + num_0_19[n1]
    return number_string

def convert_number_string(number):
    number_string = ''
    if number == 1000000:
        message = 'one million'
    elif number > 1000000:
        print('to big number')
    else:

        if len(str(number)) > 3:
            n1 = number // (10**3)
            number_string += convert_number_string_100(n1) + ' thousand '
        n0 = number % (10**3)
        number_string += convert_number_string_100(n0)
    return number_string



#number = int(input("input a number: "))
print(convert_number_string(int(input("input a number: "))).capitalize())

