'''
Напишите программу, 
которая с помощью модуля random 
моделирует броски монеты. 
Программа принимает на вход количество попыток 
и выводит результаты бросков: 
Орел или Решка (каждое на отдельной строке).

Примечание. 
Например, при n=7 ваша программа может выводить:
Орел
Решка
Решка
Орел
Орел
Орел
Решка
'''

# example
import random
n = int(input())    # количество попыток

# review 1
import random
n = int(input())
for _ in range(n):
    if random.randint(n, n**2) % 2 == 0:
        print("Орел")
    else:
        print("Решка")

# review 2
import random
n = int(input())
print(*['Решка' if random.randint(0,1) == 1 else 'Орел' for _ in range(n)],sep='\n')