'''Математические функции
Напишите программу, 
которая принимает число и название функции, 
а выводит результат применения функции к данному числу.

Список возможных функций:
    квадрат: функция принимает число и возвращает его квадрат;
    куб: функция принимает число и возвращает его куб;
    корень: функция принимает число и возвращает корень квадратный из этого числа;
    модуль: функция принимает число и возвращает его модуль;
    синус: функция принимает число (в радианах) и возвращает синус этого числа.

На вход программе подается целое число и название функции, 
записанные на отдельных строках.

Программа должна выдать результат применения функции к числу.

Примечание. 
Решите задачу без использования условного оператора.
'''

# review 1
from math import sin

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def root(num):
    return num ** 0.5

def module(num):
    return abs(num)

def sinus(num):
    return sin(num)

func_map = {
    'квадрат': square,
    'куб': cube,
    'корень': root,
    'модуль': module,
    'синус': sinus
    }

def calculate(num, func_name):
    return func_map[func_name](num)

num = int(input())
func_name = input().strip().lower()
print(calculate(num, func_name))


# review 2
import math

def pwr(p):
  def numpower(n):
    return n**p
  return numpower

func_map = {"квадрат": pwr(2), "куб": pwr(3), "корень": pwr(0.5), "модуль": abs, "синус": math.sin}

num = int(input())
func_name = input().strip().lower()
print(func_map[func_name](num))