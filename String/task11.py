# 11  Скільки разів в рядку, введеним користувачем, зустрічається вказане слово?
# Three one two one, and three one

def word_in_string(string, word):
    qty = string.split().count(word)
#or    qty = re.findall(r'\b{}\b'.format(word), string)  How it work? But before import re
    return qty

string = str(input('Input a string: '))
word = str(input('Input a word: '))

print(word.capitalize() + ' happends '+ str(word_in_string(string, word)) +' times in the string.')
