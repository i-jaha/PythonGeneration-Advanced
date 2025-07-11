'''
Вывести матрицу 2
На вход программе подаются два натуральных числа n и m, 
каждое на отдельной строке — количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; 
подряд идут элементы сначала первой строки, затем второй, и так далее.
Напишите программу, которая считывает элементы матрицы один за другим, 
выводит их в виде матрицы, выводит пустую строку, 
и снова ту же матрицу, но уже поменяв местами строки со столбцами: 
первая строка выводится как первый столбец, и так далее.

На вход программе подаются два числа n и m – количество строк и столбцов в матрице, 
далее идут n×m слов, каждое на отдельной строке.

Программа должна вывести считанную матрицу, 
за ней пустую строку и ту же матрицу, но поменяв местами строки со столбцами. 
Элементы матрицы разделять одним пробелом.
'''

n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)

print()

for col in range(m):
    for row in range(n):
        print(matrix[row][col], end=' ')
    print()