'''
Напишите функцию is_num(), 
используя синтаксис анонимных функций, 
которая принимает строковый аргумент 
и возвращает значение True, 
если переданный аргумент является числом 
(целым или вещественным), 
или False в противном случае.

Примечание 1. 
Следующий программный код:
    print(is_num('10.34ab'))
    print(is_num('10.45'))
    print(is_num('-18'))
    print(is_num('-34.67'))
    print(is_num('987'))
    print(is_num('abcd'))
    print(is_num('123.122.12'))
    print(is_num('-123.122'))
    print(is_num('--13.2'))
    print(is_num('1-1'))
должен выводить:
    False
    True
    True
    True
    True
    False
    False
    True
    False
    False

Примечание 2. 
Неотрицательные числа — это положительные числа и число нуль.

Примечание 3. 
Вызывать анонимную функцию не нужно.
'''

# review 1
is_num = lambda x: x.replace('.', '', 1).replace('-', '', 1).isdigit() and x.rfind('-') <= 0

# review 2
is_non_negative_num = lambda x: x.replace('.', '', 1).isdigit()
is_num = lambda x: is_non_negative_num(x[1:]) if x[0] == '-' else is_non_negative_num(x)