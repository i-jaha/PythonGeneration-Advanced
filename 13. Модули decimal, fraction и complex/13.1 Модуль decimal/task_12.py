"""
Дополните приведенный код так,
чтобы он вывел сумму
наибольшей и наименьшей цифры Decimal числа.

Подсказка
Используйте метод as_tuple().
"""

# example
# from decimal import *
# num = Decimal(input())

# review
from decimal import *
num = Decimal(input())
if -1 < num < 1:
    num = num.as_tuple()
    print(max(num.digits))
else:
    num = num.as_tuple()
    print(max(num.digits) + min(num.digits))