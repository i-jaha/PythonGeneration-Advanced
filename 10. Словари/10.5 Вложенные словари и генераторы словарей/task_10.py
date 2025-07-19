'''
В переменной s хранится строка пар число:слово. 
Дополните приведенный код, 
используя генератор, так, 
чтобы получить словарь result , 
в котором числа будут ключами, 
а слова – значениями.

Примечание 1. 
Ключи словаря должны быть целыми числами (иметь тип int), 
значения – строками (иметь тип str).

Примечание 2. 
Выводить содержимое словаря result не нужно.
'''

# example
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {}

# review 1
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(i.split(":")[0]):i.split(":")[1] for i in s.split()}

# review 2
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(key):value for key, value in [i.split(":") for i in s.split()]}