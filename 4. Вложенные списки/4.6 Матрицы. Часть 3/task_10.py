'''Заполнение спиралью 🌀🌶️🌶️
На вход программе подаются два натуральных числа n и m. 
Напишите программу, которая создает матрицу размером n×m, 
заполнив ее "спиралью" в соответствии с образцом.

На вход программе на одной строке подаются два натуральных числа n и m – 
количество строк и столбцов в матрице.

Программа должна вывести матрицу в соответствии образцом.

Примечание. 
Для вывода элементов матрицы как в примерах 
отводите ровно 3 символа на каждый элемент. 
Для этого используйте строковый метод ljust(). 
Можно обойтись и без ljust(), система примет и такое решение. 😇
'''

nums = [int(i) for i in input().split()]
n, m = nums[0], nums[1]
matrix = [[0 for _ in range(m)] for _ in range(n)]
num = 1
top, bottom = 0, n - 1
left, right = 0, m - 1

while num <= n * m:
    # Слева направо
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1

    # Сверху вниз
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Справа налево
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1

    # Снизу вверх
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for row in matrix:
    print(*[str(x).ljust(3) for x in row])