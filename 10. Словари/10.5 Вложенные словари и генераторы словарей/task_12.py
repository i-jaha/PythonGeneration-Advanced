"""
Дополните приведенный код,
используя генератор, так,
чтобы получить словарь result,
в котором ключом будет строка – элемент списка words,
а значением – список соответствующих кодов ASCII символов данной строки.

Примечание 1.
Если бы список words имел вид: words = ['yes', 'hello'],
то результатом был бы словарь
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}

Примечание 2.
Для получения ASCII кода символа используйте функцию ord().

Примечание 3.
Выводить содержимое словаря result не нужно.
"""

# example
words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik", "beegeek"]
result = {}

# review
words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik", "beegeek"]
result = {w: [ord(ch) for ch in w] for w in words}
print(result)