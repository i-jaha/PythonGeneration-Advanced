'''
Предикат делимости
Напишите функцию func(num1, num2), 
принимающую в качестве аргументов два натуральных числа num1 и num2 
и возвращающую значение True, 
если число num1 делится без остатка на число num2 
и False в противном случае.

Результатом вывода программы должно быть "делится" 
(если функция func() вернула True) 
или "не делится" (если функция func() вернула False).
'''

# # example
# # объявление функции
# def func(num1, num2):
#     pass
# # считываем данные
# num1, num2 = int(input()), int(input())
# # вызываем функцию
# if func(num1, num2):
#     print()
# else:
#     print()

# review
def func(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

num1, num2 = int(input()), int(input())

if func(num1, num2):
    print("делится")
else:
    print("не делится")