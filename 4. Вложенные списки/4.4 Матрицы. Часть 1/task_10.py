'''
След матрицы ↘️
Следом квадратной матрицы называется сумма элементов главной диагонали. 
Напишите программу, которая выводит след заданной квадратной матрицы.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы (целые числа) построчно через пробел.

Программа должна вывести одно число – след заданной матрицы.
'''

# review 1
n = int(input())
matrix = [input().split() for i in range(n)]
sm = 0
for row in range(n):
    for col in range(n):
        if row == col:
            sm += int(matrix[row][col])
print(sum)




# review 2
n = int(input())
sm = 0
for elem in range(n):
    matrix = input().split()
    sm += int(matrix[elem])
print(sm)