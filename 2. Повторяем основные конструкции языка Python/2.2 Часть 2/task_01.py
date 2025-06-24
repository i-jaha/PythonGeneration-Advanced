'''
Координатные четверти
Дан набор точек на координатной плоскости. 
Необходимо подсчитать и вывести количество точек, 
лежащих в каждой координатной четверти.

В первой строке записано количество точек. 
Каждая следующая строка состоит из двух целых чисел – координат точки 
(сначала абсцисса – x, затем ордината – y), разделенных символом пробела.

Программа должна вывести количество точек, лежащих в каждой координатной четверти, 
как в примерах.

Примечание. 
Учтите, что точки, лежащие на осях координат, 
не принято относить к какой-либо координатной четверти.
'''

# option 1
n = int(input())
first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0
for i in range(1, n+1):
    x, y = input().split(" ")
    x, y = int(x), int(y)
    if x > 0 and y > 0:
        first_quarter += 1
    elif x < 0 and y > 0:
        second_quarter += 1
    elif x < 0 and y < 0:
        third_quarter += 1
    elif x > 0 and y < 0:
        fourth_quarter += 1
print(f"Первая четверть: {first_quarter}")
print(f"Вторая четверть: {second_quarter}")
print(f"Третья четверть: {third_quarter}")
print(f"Четвертая четверть: {fourth_quarter}")




# option 2
n = int(input())
count = [0, 0, 0, 0]
names = ['Первая четверть:', 'Вторая четверть:', 
         'Третья четверть:', 'Четвертая четверть:']
for _ in range(n):
    x, y = [int(num) for num in input().split()]
    if x > 0 and y > 0:
        count[0] += 1
    elif x < 0 and y > 0:
        count[1] += 1
    elif x < 0 and y < 0:
        count[2] += 1
    elif x > 0 and y < 0:
        count[3] += 1
        
for i in range(4):
    print(names[i], count[i])