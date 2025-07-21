'''
Напишите программу, 
которая с помощью модуля random 
перемешивает случайным образом содержимое матрицы 
(двумерного списка).

Примечание. 
Выводить содержимое матрицы не нужно.
'''

# example
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

# review 1
import random
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
for i in range(len(matrix)):
    random.shuffle(matrix[i])
    if i == (len(matrix)-1):
        random.shuffle(matrix)
print(*matrix)

# review 2
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
[random.shuffle(row) for row in matrix]
random.shuffle(matrix)
print(*matrix)