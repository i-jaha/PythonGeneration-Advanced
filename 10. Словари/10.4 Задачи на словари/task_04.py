'''Словарь синонимов
Вам дан словарь, 
состоящий из пар слов-синонимов. 
Повторяющихся слов в словаре нет. 
Напишите программу, 
которая для одного данного слова определяет его синоним.

На вход программе подается 
количество пар синонимов n. 
Далее следует n строк, 
каждая строка содержит два слова-синонима. 
После этого следует одно слово, 
синоним которого надо найти.

Программа должна вывести одно слово, синоним введенного.

Примечание 1. 
Гарантируется, 
что синоним введенного слова существует в словаре.

Примечание 2. 
Все слова в словаре начинаются с заглавной буквы.
'''

synonyms = {}
for _ in range(int(input())):
    w1, w2 = input().split()
    synonyms[w1], synonyms[w2] = w2, w1
print(synonyms[input().strip().capitalize()])