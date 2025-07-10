''' Латинский квадрат 🌶️
Латинским квадратом порядка n называется квадратная матрица 
размером n×n, каждая строка и каждый столбец которой 
содержат все числа от 1 до n. 
Напишите программу, которая проверяет, 
является ли заданная квадратная матрица латинским квадратом.

На вход программе подаётся натуральное число n — 
количество строк и столбцов в матрице, 
затем элементы матрицы: 
n строк, по n чисел в каждой, разделённые пробелами.

Программа должна вывести слово YES, 
если матрица является латинским квадратом, 
и слово NO, если не является.
'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]

is_latin = True
required = list(range(1, n + 1))

for row in matrix:
    if sorted(row) != required:
        is_latin = False
        break

if is_latin:
    for j in range(n):
        col = [matrix[i][j] for i in range(n)]
        if sorted(col) != required:
            is_latin = False
            break

print("YES" if is_latin else "NO")