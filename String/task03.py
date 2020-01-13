# 3 Даний текст. Здійснити в цьому тексті пошук і заміну заданої фрази.
# The second attempt

def phrase_replase(string, old_phrase, new_phrase):
    return string.replace(old_phrase, new_phrase)

string = '''Python text | replace()
replace() is an inbuilt function in Python programming language that returns a copy of the text where all  occurrences of a substring is replaced with another substring.
Syntax :
text.replace(old, new, count)
Parameters :
old – old substring you want to replace.
new – new substring which would replace the old substring.
count – the number of times you want to replace the old substring with the new substring. (Optional )
Return Value :
It returns a copy of the text where all occurrences of a substring is replaced with another substring.    '''
old_phrase = 'text'
new_phrase = 'STRING'
print(phrase_replase(string, old_phrase, new_phrase))

#string = str(input('Input a string: ))
#old_phrase = str(input('Input an old phrase: ))
#new_phrase = str(input('Input a new phrase: ))
#print(phrase_replase(string, old_phrase, new_phrase))
