'''
Сократите дробь
Даны два натуральных числа m и n. 
Напишите программу, 
которая сокращает дробь m/n 
и выводит ее.
'''

from fractions import Fraction as F
n, m = [int(input()) for i in range(2)]
print(F(n, m))