# Користувач вводить рядок і символ. У рядку знайти всі входження цього символу і перевести його в верхній регістр,
# а також видалити частину рядка, починаючи з останнього входження цього символу і до кінця.

line_str = str(input("Input line: "))
symbol = str(input("Input symbol: "))

#n = -1
#for i in line_str:
#    if i == symbol:
#        n = line_str.index(symbol)
#        line_str.replace(symbol, symbol.upper())
#        line_str.replace('i', symbol)

line_str = list(line_str)

n = -1
for i in range(len(line_str)):
    if line_str[i] == symbol:
        line_str[i] = symbol.upper()
        n = i

line_str = line_str[0:n+1]
line_str = ''.join(line_str)

print(line_str)

