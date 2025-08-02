'''Случайные числа 🎲
Напишите программу, 
записывающую в текстовый файл random.txt 
25 случайных целых чисел в диапазоне от 
111 до 777 (включительно), 
каждое с новой строки.

На вход программе ничего не подается.

Программа должна создать файл с именем random.txt 
и записать в него случайные числа 
в соответствии с условием задачи.

Примечание 1. 
Считайте, что исполняемая программа 
и указанный файл находятся в одной папке.

Примечание 2. 
Для генерации случайных чисел используйте модуль random.
'''

# review 1
from random import randrange
with open("random.txt", "w", encoding="utf-8") as file:
    for _ in range(25):
        file.write(f"{randrange(111, 778)}\n")

# review 2
from random import randrange
with open('random.txt','w') as file:
    print(*[randrange(111,778) for _ in range(25)], sep="\n", file=file)