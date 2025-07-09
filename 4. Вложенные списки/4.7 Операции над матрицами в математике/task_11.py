'''Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в m-ую степень.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы, затем натуральное число m.

Программа должна вывести результирующую матрицу, 
разделяя элементы символом пробела.
'''

n = int(input())    # количество строк и столбцов в матрице
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())    # возводимая степень

result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

for power in range(m):
    temp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += result[i][k] * matrix[k][j]
    
    for i in range(n):
        for j in range(n):
            result[i][j] = temp[i][j]

for row in result:
    print(*row)