'''Урок информатики 👨‍💻
Даны по 10-балльной шкале оценки по информатике трех учеников. 
Напишите программу, 
выводящую множество оценок, 
которые есть и у первого, 
и у второго учеников, 
но которых нет у третьего ученика.

На вход программе подаются оценки трех учеников, 
разделенные символом пробела 
(оценки каждого ученика на отдельной строке).

Программа должна вывести множество оценок 
в порядке убывания на одной строке, 
разделенных пробелами, 
в соответствии с условием задачи.

Примечание. 
Оценка ученика находится в диапазоне от 0 до 10 включительно.
'''

s1, s2, s3 = [set(input().split()) for _ in range(3)]
print(*sorted((s1 & s2) - s3, key=int, reverse=True))