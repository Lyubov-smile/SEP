# 10 Написати функцію, яка визначає чи є рядок паліндромом (тобто рядк, який можна читати зліва направо, і справа наліво:
# «А роза упала на лапу Азора», «Аргентина манить негра»).
# Never a foot too far, even.
# Red rum, sir, is murder

def string_for_compare(string):
    string = string.lower()
    s = []
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90 or 97 <= ord(string[i]) <= 122:
            s.append(string[i])

    ru_letters = [1105, 1108, 1110, 1111, 1025, 1028, 1030, 1031, 1168, 1169]
    for i in range(len(string)):
        if 1040 <= ord(string[i]) <= 1103:
            s.append(string[i])
        elif chr(i) in ru_letters:
            s.append(string[i])
    s = ''.join(s)
    return s

def reverse(string):
    return string[::-1]

def isPalindrome(string):
    string = string_for_compare(string)
    if string == reverse(string):
        message = 'This string is a palindrome'
    else:
        message = "This string isn't a palindrome"
    return(message)

s = str(input())
print(s)
print(isPalindrome(s))
