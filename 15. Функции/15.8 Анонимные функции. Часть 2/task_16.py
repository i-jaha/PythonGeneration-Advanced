'''Значение многочлена 🌶️
Многочленом степени n называется выражение вида 
a_n*x_n + a_(n-1)*x_(n-1) + ... + a_2*x² + a₁x + a_0
где (a_{n}, a_{n-1}, ..., a_{2}, a_{1}, a_{0}) — коэффициенты многочлена (a_n = 0).
На вход программе на первой строке подаются коэффициенты многочлена, 
разделенные символом пробела и целое число x на второй строке. 
Напишите программу, которая вычисляет значение указанного многочлена 
при заданном значении x.

На вход программе на первой строке подаются коэффициенты многочлена (целые числа), 
разделенные символом пробела и целое число x на второй строке.

Программа должна вывести одно число — 
значение указанного многочлена при заданном значении x.

Примечание 1. 
Первый тест задает многочлен 
    2x^2 + 4x + 3, 
второй тест задает многочлен 
    x^6 + 2x^5 + 3x^4 + 4x^3 + 5x^2 + 6x + 7.

Примечание 2. 
Решение задачи необходимо оформить 
в виде функции evaluate(coefficients, x), 
которая принимает список коэффициентов и значение аргумента. 
Функция evaluate() должна быть реализована 
на основе встроенных функций map() и reduce().

Примечание 3. 
Не забудьте вызвать функцию evaluate(), 
чтобы вывести результат 😀.
'''

# review 1
## Horner's method
from functools import reduce

def evaluate(coefficients, x):
    return reduce(lambda acc, pair: acc + pair[0] * (x ** pair[1]),
                  zip(coefficients, reversed(range(len(coefficients)))),
                  0)

coefficients = list(map(int, input().split()))
x = int(input())

print(evaluate(coefficients, x))

# review 2
## Horner's method
from functools import reduce
evaluate = lambda coefficients, x: reduce(lambda s, a: s * x + a, coefficients, 0)
print(evaluate([*map(int, input().split())], int(input())))