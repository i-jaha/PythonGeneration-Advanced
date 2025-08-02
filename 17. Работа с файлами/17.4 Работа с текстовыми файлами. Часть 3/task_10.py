'''Нумерация строк 🔢
Вам доступен текстовый файл input.txt, 
состоящий из нескольких строк. 
Напишите программу для записи содержимого этого файла 
в файл output.txt в виде нумерованного списка, 
где перед каждой строкой стоит ее номер, символ ")" и пробел. 
Нумерация строк должна начинаться с 1.

На вход программе ничего не подается.

Программа должна создать файл с именем output.txt 
и записать в него пронумерованные строки файла input.txt.

Примечание 1. 
Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. 
Используйте встроенную функцию enumerate().

Примечание 3. 
Если бы файл input.txt содержал строки:
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
то файл output.txt имел бы вид:
    1) Beautiful is better than ugly.
    2) Explicit is better than implicit.
    3) Simple is better than complex.
    4) Complex is better than complicated.

Примечание 4. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/519126/input.txt].
'''

# review 1
with open("input.txt", "r", encoding="utf-8") as infile, \
     open("output.txt", "w", encoding="utf-8") as outfile:
    for index, line in enumerate(infile, start=1):
        outfile.write(f"{index}) {line}")

# review 2
with open('input.txt', 'r', encoding='utf-8') as infile, \
    open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.writelines([f'{i}) {j}' for i, j in enumerate(infile.readlines(), start=1)])