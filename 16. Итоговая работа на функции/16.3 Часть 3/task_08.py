'''
Напишите функцию arithmetic_operation(), 
которая принимает символ 
одной из четырех арифметических операций (+, -, *, /) 
и возвращает функцию двух аргументов для соответствующей операции.

Примечание 1. 
При условии, что функция arithmetic_operation() написана правильно, 
приведенный ниже код:
    add = arithmetic_operation('+')
    div = arithmetic_operation('/')
    print(add(10, 20))
    print(div(20, 5))
должен выводить:
30
4.0

Примечание 2. 
Вызывать функцию arithmetic_operation() не нужно, 
требуется только реализовать ее.

Примечание 3. 
Модуль operator может быть полезен 
при решении этой задачи.
'''

# review 1
import operator
def arithmetic_operation(operation):
    def func(x, y):
        if operation == '+':
            return operator.add(x, y)
        elif operation == '-':
            return operator.sub(x, y)
        elif operation == '*':
            return operator.mul(x, y)
        elif operation == '/':
            return operator.truediv(x, y)
    return func

# review 2
import operator
def arithmetic_operation(operation):
    oper = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return oper[operation]

# review 3
def arithmetic_operation(operation):
    return lambda x, y: eval(f'{x}{operation}{y}')

add = arithmetic_operation('+')
div = arithmetic_operation('/')
print(add(10, 20))
print(div(20, 5))