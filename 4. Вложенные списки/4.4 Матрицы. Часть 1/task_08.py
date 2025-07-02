'''
Вывести матрицу 1
На вход программе подаются два натуральных числа n и m, 
каждое на отдельной строке – количество строк и столбцов в матрице. 
Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; 
подряд идут элементы сначала первой строки, затем второй, и так далее.
Напишите программу, которая сначала считывает элементы матрицы один за другим, 
затем выводит их в виде матрицы.

На вход программе подаются два числа n и m – количество строк и столбцов в матрице, 
далее идут n×m слов, каждое на отдельной строке.

Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
'''

# review 1
def create_matrix(n: int, m: int):
    matrix = [[input() for c in range(m)] for r in range(n)]
    return matrix

def print_matrix(matrix, n: int, m: int):
    for r in range(n):
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()

n, m = int(input()), int(input())
new_matrix = create_matrix(n, m)
print_matrix(new_matrix, n, m)

# review 2
n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]
for row in matrix:
    print(*row)