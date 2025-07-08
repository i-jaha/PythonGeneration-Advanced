'''Заполнение змейкой 🐍
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером n×m, 
заполнив ее "змейкой" в соответствии с образцом.

На вход программе на одной строке подаются два натуральных числа n и m – 
количество строк и столбцов в матрице.

Программа должна вывести указанную матрицу в соответствии с образцом.

Примечание. 
Для вывода элементов матрицы как в примерах 
отводите ровно 3 символа на каждый элемент. 
Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), система примет и такое решение. 😇
'''

# review 1
nums = [int(i) for i in input().split()]
n, m = nums[0], nums[1]
matrix = []
num = 1

for row in range(n):
    new_row = []
    for col in range(m):
        new_row.append(num)
        num += 1
    if row % 2 != 0:
        new_row.reverse()
    matrix.append(new_row)

for row in matrix:
    print(*[str(x).ljust(3) for x in row])




# review 2
n, m = [int(i) for i in input().split()]
matrix = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * m + j + 1
    if i % 2:
        matrix[i].reverse()

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()