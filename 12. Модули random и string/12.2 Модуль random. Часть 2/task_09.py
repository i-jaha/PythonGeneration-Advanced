'''
Напишите программу, 
которая с помощью модуля random 
генерирует 100 случайных номеров лотерейных билетов 
и выводит их, каждый на отдельной строке. 
Обратите внимание, 
вы должны придерживаться следующих условий:
    номер не может начинаться с нулей;
    номер лотерейного билета должен состоять из 7 цифр;
    все 100 лотерейных билетов должны быть различными.
'''

def random_lottery_ticket(number: int = 100):
    import random

    lottery_tickets = set()
    while len(lottery_tickets) < number:
        ticket = random.randint(1000000, 9999999)
        lottery_tickets.add(ticket)

    for ticket in lottery_tickets:
        print(ticket)

random_lottery_ticket()