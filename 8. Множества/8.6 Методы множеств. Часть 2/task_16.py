'''Общие цифры
На вход программе подаются натуральное число n, 
а затем n различных натуральных чисел, 
каждое на отдельной строке. 
Напишите программу, 
которая выводит все общие цифры 
в порядке возрастания 
у всех введенных чисел.

На вход программе подаются натуральное число n (n≥1), 
а затем n различных натуральных чисел, 
каждое на отдельной строке.

Программа должна вывести цифры 
в соответствии с условием задачи. 
Если общих цифр нет, 
то ничего выводить не нужно.
'''

n = int(input())
common_digits = set(input())
if n >= 1:
    for _ in range(n - 1):
        number = set(input())
        common_digits &= number
    print(*sorted(int(d) for d in common_digits))
else:
    "Enter a natural number greater than or equal to 1"