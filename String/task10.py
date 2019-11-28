# 10 Написати функцію, яка визначає чи є рядок паліндромом (тобто рядк, який можна читати зліва направо, і справа наліво:
# «А роза упала на лапу Азора», «Аргентина манить негра»).
# Never a foot too far, even.
# Red rum, sir, is murder
# Was it a car or a cat I saw?


def reverse(string):
    return string[::-1]


def isPalindrome(string):
    string = string.lower()
    string = string.replace(' ', '')
    string = string.replace(',', '')
    string = string.replace('.', '')
    string = string.replace(':', '')
    string = string.replace('?', '')
    string = string.replace('!', '')
    string = string.replace('-', '')
    if string == reverse(string):
        message = 'This string is a palindrome'
    else:
        message = "This string isn't a palindrome"
    return message

s = str(input())
print(isPalindrome(s))

# in file 10_2 is program without function
