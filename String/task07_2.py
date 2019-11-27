# 7 Написати функцію, що перетворює дробове або ціле число в рядок.

# converts a number to a string
num2words1 = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
              10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
              17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
              90: 'Ninety'}


# num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def convert_number_string(number):
    number_string = ''
    if number == 1000000:
        message = 'One Million'
    elif number > 1000000:
        print('to big number')
    elif number == 0:
        print('Zero')
    else:
        n1 = number // (10 ** 5)
        if n1 > 0:
            number_string += num2words1[n1] + ' Hundred '
        number = number % (10 ** 5)
        n1 = number // (10 ** 3)
        number = number % (10 ** 3)
        if n1 < 20:
            number_string += num2words1[n1] + ' Thousand '
        elif n1 > 19:
            n2 = n1 - (n1 % 10)
            n1 = n1 % 10
            number_string += num2words2[n2] + ' ' + num2words1[n1] + ' Thousand '
        if number_string == ' Thousand ':
            number_string = ''
        n1 = number // (10 ** 2)
        n2 = number % (10 ** 2)
        if n1 > 0:
            number_string += num2words1[n1] + ' Hundred '
        if n2 < 20:
            number_string += num2words1[n2]
        elif n2 > 19:
            n1 = n2 % 10
            n2 = n2 - n1
            number_string += num2words2[n2] + ' ' + num2words1[n1]
    return number_string


number = int(input("input a number: "))
# print(convert_number_string(int(input("input a number: "))))
print(convert_number_string(number))
