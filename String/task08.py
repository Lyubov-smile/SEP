# 9  З клавіатури вводиться ціле число в діапазоні від 0 до 1000000.
# Необхідно вивести його прописний стрічковий еквівалент.

''' # converts a number to a string
num_0_19 = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
            'Ten': 10, 'Eleven': 11, 'Twelve': 12, 'Thirteen': 13, 'Fourteen': 14, 'Fifteen': 15, 'Sixteen': 16,
            'Seventeen': 17, 'Eighteen': 18, 'Nineteen': 19}

num_20_90 = {'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60, 'Seventy': 70, 'Eighty': 80,
             'Ninety': 90}
'''

num_0_19 = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
            'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
            'seventeen': 17, 'eighteen': 18, 'nineteen': 19}
num_20_90 = {'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80,
             'ninety': 90}

def str_to_n_100(string):
    number = 0
    if 'hundred' in string:
        string = string.split(' hundred ')
        number += num_0_19[string[0]] * 100
        print(string[0], string[-1])
    if 'ty' in string[-1]:
        string = string[-1].split(' ')
        number += num_20_90[string[0]]
        number += num_0_19[string[-1]]
    else:
        number += num_0_19[string[-1]]
    return(number)


def str_to_number(string):
    number = 0
    if 'thousand' in string:
        string = string.split(' thousand ')
        number += str_to_n_100(string[0]) * 1000 + str_to_n_100(string[-1])
    else:
        number += str_to_n_100(string)
    return(number)


# string = 'seven hundred eighty nine thousand one hundred twenty three'
# string = 'one hundred nineteen thousand six hundred forty five'

string = str(input('Input your number: ')).lower()
print(string)
print(str_to_number(string))


