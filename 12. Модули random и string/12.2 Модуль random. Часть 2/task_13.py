'''Генератор паролей 1
Напишите программу, 
которая с помощью модуля random 
генерирует n паролей длиной m символов, 
состоящих из строчных и прописных английских букв и цифр, 
кроме тех, которые легко перепутать между собой:
    «l» (L маленькое);
    «I» (i большое);
    «1» (цифра);
    «o» и «O» (маленькая и большая буквы);
    «0» (цифра).

На вход программе подаются два числа n и m, 
каждое на отдельной строке.

Программа должна вывести n паролей 
длиной m символов 
в соответствии с условием задачи, 
каждый на отдельной строке.

Примечание 1. 
Считать, что числа n и m всегда таковы, 
что требуемые пароли сгенерировать возможно.

Примечание 2. 
В каждом пароле необязательно должна присутствовать 
хотя бы одна цифра и буква в верхнем и нижнем регистре.

Примечание 3. 
Решение задачи удобно оформить в виде двух вспомогательных функций:
    - функция generate_password(length) – 
    возвращает случайный пароль длиной length символов;
    - функция generate_passwords(count, length) – 
    возвращает список, состоящий из count случайных паролей 
    длиной length символов.

Примечание 4. 
Приведенные ниже тесты – 
это лишь образцы возможного ответа. 
Возможны и другие способы генерации паролей.
'''

import random
import string

chars = [c for c in (string.ascii_letters + string.digits) if c not in 'lI10oO']

def generate_password(length):
    return ''.join(random.choice(chars) for _ in range(length))

def generate_passwords(count, length):
    for _ in range(count):
        print(generate_password(length))

n, m = int(input()), int(input())

generate_passwords(n, m)