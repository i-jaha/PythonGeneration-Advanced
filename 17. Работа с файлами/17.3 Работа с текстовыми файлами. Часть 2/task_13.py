'''Random name and surname 🎲
Вам доступны два текстовых файла 
first_names.txt и last_names.txt, 
один с именами, другой с фамилиями.
Напишите программу, 
которая c помощью модуля random 
создает 3 случайные пары имя + фамилия, 
а затем выводит их, 
каждую на отдельной строке.

На вход программе ничего не подается.

Программа должна вывести текст в формате, 
приведенном в примере.


Примечание 1. 
Если бы файлы first_names.txt и last_names.txt содержали строки:
    Aaron
    Abdul
    Abe
    Abel
    Abraham
    Albert
и
    Abramson
    Adamson
    Adderiy
    Addington
    Adrian
    Albertson
    Einstein
то результатом могло быть:
Abdul Albertson
Abel Adamson
Albert Einstein

Примечание 2. 
Указанные файлы можно скачать 
по ссылкам 
((имена)[https://stepik.org/media/attachments/lesson/530408/first_names.txt], 
(фамилии)[https://stepik.org/media/attachments/lesson/530408/last_names.txt]). 
'''

from random import choice
with open("first_names.txt", "rt", encoding="utf-8") as f_names, \
    open("last_names.txt", "rt", encoding="utf-8") as l_names:
    first_names = [name.strip() for name in f_names if name.strip()]
    last_names = [surname.strip() for surname in l_names if surname.strip()]
for _ in range(3):
    print(f"{choice(first_names)} {choice(last_names)}")