'''Длинные строки ↔️
Вам доступен текстовый файл lines.txt, 
в котором записаны строки текста. 
Напишите программу, 
которая выводит все строки 
наибольшей длины из файла, 
не меняя их порядок.

На вход программе ничего не подается.

Программа должна вывести строки указанного файла, 
имеющие наибольшую длину, 
не меняя их порядка.

Примечание 1. 
Считайте, что исполняемая программа 
и указанный файл находятся в одной папке.

Примечание 2. 
Используйте менеджер контекста. 🙂

Примечание 3. 
Если бы файл lines.txt содержал строки:
    One
    Twenty one
    Two
    Twenty two
то результатом будет:
    Twenty one
    Twenty two

Примечание 4. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/530408/lines.txt]. 
'''

# review 1
with open("lines.txt", "r", encoding="utf-8") as file:
    lines = [line.rstrip('\n') for line in file]
    max_len = max(map(len, lines))
    for line in lines:
        if len(line) == max_len:
            print(line)

# review 2
with open("lines.txt", "r", encoding="utf-8") as file:
    max_len = 0
    for line in file:
        max_len = max(max_len, len(line.rstrip('\n')))
    
    file.seek(0)
    
    for line in file:
        if len(line.rstrip('\n')) == max_len:
            print(line.rstrip('\n'))