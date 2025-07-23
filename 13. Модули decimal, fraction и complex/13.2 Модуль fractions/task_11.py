'''Сумма дробей 2
На вход программе подается натуральное число n. 
Напишите программу, 
которая вычисляет и выводит рациональное число, 
равное значению выражения:
    1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) +...+ 1/(n!)

На вход программе подается натуральное число n.

Программа должна вывести ответ на задачу.

Примечание 1. 
Результирующая дробь должна быть несократимой.

Примечание 2. 
Для вычисления факториала 
можно использовать функцию factorial 
из модуля math.
'''

# review 1
from fractions import Fraction as F
from math import factorial as f
n = int(input())
result = F(0)
for i in range(1, n+1):
    result += F(1, f(i))
print(result)

# review 2
from fractions import Fraction as F
from math import factorial as f
print(sum(F(1, f(i)) for i in range(1, int(input()) + 1)))