'''
Почтовый индекс в Латверии имеет вид: 
    LetterLetterNumber_NumberLetterLetter
где Letter – заглавная буква английского алфавита, 
Number – число от 0 до 99 (включительно).
Напишите функцию generate_index(), 
которая с помощью модуля random 
генерирует и возвращает случайный корректный почтовый индекс Латверии.

Примечание 1. 
Пример правильного (неправильного) индекса Латверии:
    AB23_56VG          # правильный
    V3F_231GT          # неправильный

Примечание 2. 
Обратите внимание на символ _ в почтовом индексе.

Примечание 3. 
Вызывать функцию generate_index() не нужно, 
требуется только реализовать.
'''

import random
import string
def generate_index():
    index = ""
    for i in range(7):
        if i in [0, 1, 5, 6]:
            index += random.choice(string.ascii_uppercase)
        elif i in [2, 4]:
            index += f"{random.randint(0, 99):02}"
        else:
            index += "_"
    return index
print(generate_index())