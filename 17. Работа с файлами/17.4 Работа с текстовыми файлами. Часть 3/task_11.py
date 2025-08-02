'''Подарок на новый год 🎁
Вам доступен текстовый файл class_scores.txt 
с оценками за итоговый тест на строках вида: 
фамилия оценка (фамилия и оценка разделены пробелом). 
Оценка - целое число от 0 до 100 включительно.

Напишите программу 
для добавления 5 баллов к каждому результату теста 
и вывода фамилий и новых результатов тестов 
в файл new_scores.txt.

На вход программе ничего не подается.

Программа должна создать файл с именем new_scores.txt 
в соответствии с условием задачи.

Примечание 1. 
Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. 
Если бы файл class_scores.txt содержал строки:
    Washington 83
    Adams 86
    Kingsman 100
    MacDonald 95
    Thomson 98
то файл new_scores.txt имел бы вид:
    Washington 88
    Adams 91
    Kingsman 100
    MacDonald 100
    Thomson 100

Примечание 3. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/519126/class_scores.txt].
'''

# review 1
with open("class_scores.txt", "r", encoding="utf-8") as infile, \
    open("new_scores.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        student, mark = line.strip().split()
        outfile.write(f"{student} {min(100, int(mark)+5)}\n")

# review 2
with open('class_scores.txt', encoding='utf-8') as infile, \
    open('new_scores.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        print(
            line.strip().split()[0] + ' ' + str(min(100, int(line.strip().split()[1]) + 5)), 
            file=outfile
            )