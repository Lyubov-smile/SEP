# 1 Створити метод який приймає, введену користувачем стрічку і виводить на екран статистику по цій стрічці.
# Статистика повинна включати загальну кількість символів, кількість букв (і скільки букв в верхньому регістрі
# і нижньому), кількість цифр, символів пунктуації та кількість символів пробілів.


#s = str(input('Input a string: \n'))

marks = [33, 34, 39, 40, 41, 44, 45, 46, 58, 59, 63, 91, 93]

string = '''Yes, I'll smile, indeed, through tears and weeping
... Sing my songs where evil holds its sway,
... Hopeless, a steadfast hope forever keeping,
... I shall live! You thoughts of grief, away!
1 2 3 4 5 6 7 8 9'''

count_letters = 0
count_uppercase_letters = 0
count_lowercase_letters = 0
count_space = 0
count_signs = 0
count_marks = 0
count_numbers = 0
c = 0
for i in string:
    if ord(i) == 32:
        count_space += 1
    elif 65 <= ord(i) <= 90:
        count_uppercase_letters += 1
    elif 97 <= ord(i) <= 122:
        count_lowercase_letters += 1
    elif ord(i) in marks:
        count_marks += 1
    elif 48 <= ord(i) <= 57:
        count_numbers += 1

print("Total QTY of symbols: ", len(string))
print("Uppercase: ", count_uppercase_letters)
print("Lowercase: ", count_lowercase_letters)
print("Spaces: ", count_space)
print("Punctuation marks: ", count_marks)
print("Numbers: ", count_numbers)

# If we need to calculate all symbols in text
# elif 33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(i) <= 96 or 123 <= ord(i) <= 126:
#        count_signs += 1



#line 31    elif ord(i) == 33 or ord(i) == 34 or ord(i) == 39 or ord(i) == 40 or ord(i) == 41 or ord(i) == 44 or ord(i) == 45 or ord(i) == 46 or ord(i) == 58 or ord(i) == 59 or ord(i) == 63 or ord(i) == 91 or ord(i) == 93:
