'''
Анаграмма – это слово, 
образованное путем перестановки букв, 
составляющих другое слово.

Например, 
слова пила и липа или пост и стоп – анаграммы.

Напишите программу, 
которая считывает одно слово 
и выводит с помощью модуля random 
его случайную анаграмму.

Примечание. 
Обратите внимание на то, 
что метод shuffle() работает со списком, 
а не со строкой.
'''

import random
word = list(input())
random.shuffle(word)
print(''.join(word))