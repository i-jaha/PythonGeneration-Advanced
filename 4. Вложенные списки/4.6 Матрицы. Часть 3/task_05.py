'''Заполнение 3
На вход программе подается натуральное число n. 
Напишите программу, которая создает матрицу размером n×n, 
заполнив ее в соответствии с образцом.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице.

Программа должна вывести указанную матрицу в соответствии с образцом: 
разместить единицы на главной и побочной диагоналях, 
остальные позиции матрицы заполнить нулями.

Примечание. 
Для вывода элементов матрицы как в примерах 
отводите ровно 3 символа на каждый элемент. 
Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), 
система примет и такое решение. 😇
'''

# review 1
n = int(input())
matrix = [[0]*n for _ in range(n)]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i == j) or (i == n - j - 1):
            matrix[i][j] = 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])




# review 2
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j or i + j + 1 == n:
            matrix[i][j] = 1

for row in matrix:
    print(*row)