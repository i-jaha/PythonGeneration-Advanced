'''Интересная сортировка-2
На вход программе подается строка натуральных чисел. 
Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел 
в порядке неубывания суммы их цифр. 
При этом, если у двух чисел одинаковая сумма цифр, 
их следует вывести в порядке неубывания.

На вход программе подается строка текста, 
содержащая натуральные числа, разделенные пробелами.

Программа должна вывести отсортированный список чисел 
в соответствии с условием задачи, 
разделяя его элементы одним пробелом.

Подсказка
Вспомните, каким образом сортируются кортежи.
'''

# review 1
def sum_digits(num):
    return sum(int(digit) for digit in str(num)), num
numbers = [int(num) for num in input().split()]
print(*sorted(numbers, key=sum_digits))

# review 2
def custom_sort(numbers):
    def sum_digits(num):
        return sum(int(digit) for digit in str(num)), num
    return sorted(numbers, key=sum_digits)
numbers = [int(num) for num in input().split()]
print(*custom_sort(numbers))