'''Заполнение диагоналями ↙️🌶️
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером n×m, 
заполнив ее "диагоналями" в соответствии с образцом.

На вход программе на одной строке подаются два натуральных числа n и m – 
количество строк и столбцов в матрице.

Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. 
Для вывода элементов матрицы как в примерах 
отводите ровно 3 символа на каждый элемент. 
Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), система примет и такое решение. 😇
'''

nums = [int(i) for i in input().split()]
n, m = nums[0], nums[1]
num = 1
matrix = [[0 for _ in range(m)] for _ in range(n)]

for q in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i + j == q:
                matrix[i][j] = num
                num += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])