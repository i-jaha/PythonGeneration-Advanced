'''
Зеркальное отображение 🦋

Дана квадратная матрица чисел. 
Напишите программу, которая зеркально отображает её элементы 
относительно горизонтальной оси симметрии.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы построчно через пробел.

Программа должна вывести матрицу, 
в которой зеркально отображены элементы 
относительно горизонтальной оси симметрии.
'''

# review 1
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
for r in range(n // 2):
    matrix[r], matrix[n-r-1] = matrix[n-r-1], matrix[r]
for r in range(n):
    print(*matrix[r])

# review 2
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix.reverse()
for r in range(n):
    print(*matrix[r])