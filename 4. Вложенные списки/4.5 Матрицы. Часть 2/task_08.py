'''
Поворот матрицы 🔁

Напишите программу, которая поворачивает квадратную матрицу чисел 
на 90∘ по часовой стрелке.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы построчно через пробел.

Программа должна вывести результат на экран, 
числа должны быть разделены одним пробелом.
'''

# review 1
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
rotated = [[0] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        rotated[c][n-1-r] = matrix[r][c]
for row in rotated:
    print(*row)




# review 2
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
[print(*[matrix[n-c-1][r] for c in range(n)]) for r in range(n)]