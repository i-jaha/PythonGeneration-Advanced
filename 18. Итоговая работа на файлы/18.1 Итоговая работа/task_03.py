'''Goooood students 😇
Вам доступен текстовый файл grades.txt, 
содержащий оценки студента за три теста в каждом из триместров. 
Строки файла имеют вид: фамилия оценка_1 оценка_2 оценка_3.
Напишите программу для подсчета количества студентов, 
сдавших все три теста. 
Тест считается сданным, 
если количество баллов по нему не меньше 65.

На вход программе ничего не подается.

Программа должна вывести количество студентов, сдавших все три теста.

Примечание 1. 
Считайте, что исполняемая программа 
и указанный файл находятся в одной папке.

Примечание 2. 
Если бы файл grades.txt содержал строки:
    Washington 83 77 54
    Adams 86 69 90
    Jacobson 50 49 71
    MacDonald 100 99 100
    Berrington 66 67 64
то результатом будет:
    2

Примечание 3. 
Указанный файл можно скачать 
по [ссылке](https://stepik.org/media/attachments/lesson/448983/grades.txt).
'''

# review 1
count = 0
with open("grades.txt", "rt", encoding="utf-8") as infile:
    for line in infile:
        parts = line.split()
        surname, marks = parts[0], [int(i) for i in parts[1:]]
        if min(marks) >= 65:
            count += 1
print(count)

# review 2
with open("grades.txt", "r", encoding="utf-8") as infile:
    count = sum(1 for line in infile if min(map(int, line.split()[1:])) >= 65)
print(count)