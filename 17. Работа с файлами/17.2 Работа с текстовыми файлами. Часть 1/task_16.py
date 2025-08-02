'''Общая стоимость 💰
Вам доступен текстовый файл prices.txt 
с информацией о заказе из интернет-магазина. 
В нем каждая строка с помощью символа табуляции (\t) 
разделена на три колонки:
    наименование товара;
    количество товара (целое число);
    цена (в рублях) товара за 1 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа.

На вход программе ничего не подается.

Программа должна вывести общую стоимость заказа.

Примечание 1. 
Считайте, что исполняемая программа и указанный файл находятся в одной папке.

Примечание 2. 
Не забудьте закрыть файл. 🙂

Примечание 3. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/519125/prices.txt].
'''

# review 1
file = open("prices.txt", "rt", encoding="utf-8")
total = 0
for line in file.readlines():
    name, qty, price  = line.strip().split("\t")
    total += int(qty) * int(price)
print(total)
file.close()

# review 2
file = open('prices.txt')
lines = map(str.split, map(str.strip, file))
print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
file.close()