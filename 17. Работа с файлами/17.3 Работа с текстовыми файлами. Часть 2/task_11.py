'''Сумма чисел в файле
Вам доступен текстовый файл nums.txt. 
В файле могут быть записаны 
целые неотрицательные числа и все что угодно. 
Числом назовем последовательность одной и более цифр, 
идущих подряд (число всегда неотрицательно).
Напишите программу, 
которая вычисляет сумму всех чисел, 
записанных в файле.

На вход программе ничего не подается.

Программа должна вывести сумму всех чисел, записанных в файле.

Примечание 1. 
Если бы файл nums.txt содержал строки:
    123   jhjk
    bhjip456qwerty
    1x2y3 4 5 6
    sfsd 0 dfgfd
    10abc20de30pop5 5 5 5
то результатом было бы:
    680
Примечание 2. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/530408/nums.txt]. 
'''

# review 1
total = 0
with open("nums.txt", "r", encoding="utf-8") as file:
    for line in file:
        number = ''
        for char in line:
            if char.isdigit():
                number += char
            else:
                if number != '':
                    total += int(number)
                    number = ''
        if number:
            total += int(number)
print(total)

# review 2
with open('numbers.txt', encoding='utf-8') as file:
    line = ''.join(c if c.isdigit() else ' ' for c in file.read())
    print(sum(map(int, line.split())))