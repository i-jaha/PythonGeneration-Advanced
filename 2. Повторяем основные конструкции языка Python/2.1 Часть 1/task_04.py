'''
Стоимость строки
Дана строка текста. 
Напишите программу для подсчета стоимости строки, 
исходя из того, что один любой символ (в том числе пробел) стоит 60 копеек. 
Ответ дайте в рублях и копейках в соответствии с примерами.

На вход программе подается строка текста.

Программа должна вывести стоимость строки.
'''

s = input()
cost = len(s) * 60
print(f'{cost // 100} р. {cost % 100} коп.')