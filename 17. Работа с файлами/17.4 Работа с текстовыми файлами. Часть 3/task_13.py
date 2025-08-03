'''Конкатенация файлов 🗃️🌶️
На вход программе подается натуральное число n 
и n строк с названиями файлов. 
Напишите программу, которая создает файл output.txt 
и выводит в него содержимое всех файлов, не меняя их порядка.

На вход программе подаются натуральное число n и 
n строк названий существующих файлов.

Программа должна создать файл с именем output.txt 
в соответствии с условием задачи.

Примечание 1. 
Считайте, что исполняемая программа и 
указанные файлы находятся в одной папке.

Примечание 2. 
Если бы на вход было подано 2 файла, и 
эти файлы содержали бы строки 
(обратите внимание, что в конце первого файла нет перевода строки)
    Early in the morning
и
    we
    went
    for mushrooms
то результирующий файл output.txt 
выглядел бы следующим образом:
Early in the morningwe
went
for mushrooms
'''

# review 1
n = int(input())
filenames = [input() for _ in range(n)]
with open("output.txt", "w", encoding="utf-8") as outfile:
    for name in filenames:
        with open(name, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())

# review 2
with open('output.txt', 'w') as outfile:
    for _ in range(int(input())):
        with open(input()) as infile:
            outfile.write(infile.read())