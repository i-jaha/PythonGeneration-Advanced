'''
Разбиение на чанки 🌶️
На вход программе подаются две строки: 
на одной – символы, на другой – число n. 
Из первой строки формируется список.
Реализуйте функцию chunked(), которая принимает на вход список и число, 
задающее размер чанка (куска), 
а возвращает список из чанков (кусков) указанной длины.

На вход программе подаются строка текста, содержащая символы, 
разделенные символом пробела, и число n на отдельной строке.

Программа должна вывести указанный вложенный список.

Примечание. 
Не забудьте вызвать функцию chunked(), 
чтобы вывести результат. 😀
'''

def chunked(s, n):
    list_chunk = []
    for i in range(0, len(s), n):
        list_chunk.append(s[i:(i+n)])
    return list_chunk

s = input().split()
n = int(input())

print(chunked(s, n))