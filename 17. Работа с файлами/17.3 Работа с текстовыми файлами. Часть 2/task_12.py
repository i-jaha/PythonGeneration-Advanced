'''Статистика по файлу 📊
Вам доступен текстовый файл file.txt, 
набранный латиницей. 
Напишите программу, 
которая выводит количество 
букв латинского алфавита, слов и строк. 
Выведите три найденных числа в формате, 
приведенном в примере.

На вход программе ничего не подается.

На вход программе ничего не подается.

Примечание 1. 
Если бы файл file.txt содержал строки:
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
то результатом было бы:
    Input file contains:
    108 letters 
    20 words 
    4 lines 

Примечание 2. 
Словом называется последовательность из непробельных символов. 
Например, строка
    abc a21 67pop    qwert bo7ok 83456
содержит 6 слов: abc, a21, 67pop, qwert, bo7ok, 83456.

Примечание 3. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/530408/file.txt].
'''

# review 1
with open("file.txt", "rt", encoding="utf-8") as file:
    lines = len(file.readlines())
    file.seek(0)
    content = file.read().strip().split()
    words = len(content)
    letters = 0
    for word in content:
        for ch in word:
            if ch.isalpha():
                letters += 1
    print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines")

# review 2
letters = words = lines = 0
with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        lines += 1
        words += len(line.split())
        letters += sum(1 for ch in line if ch.isalpha())
print(f"Input file contains:\n{letters} letters\n{words} words\n{lines} lines")
