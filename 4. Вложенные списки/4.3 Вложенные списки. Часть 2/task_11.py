'''
Треугольник Паскаля 2
На вход программе подается натуральное число n. 
Напишите программу, которая выводит первые n строк треугольника Паскаля.

На вход программе подается число n (n≥1).

Программа должна вывести первые n строк треугольника Паскаля, 
каждую на отдельной строке, в соответствии с образцом.
'''

def pascal(n):
    row = [1]
    for i in range(1, n + 1):
        next_val = row[-1] * (n - i + 1) // i
        row.append(next_val)
    return row

n = int(input())
for i in range(n):
    print(*pascal(i))