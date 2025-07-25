'''
Программист Тимур написал программу для работы 
с биографическими данными русских поэтов. 
Данные содержатся в кортежах вида 
(фамилия, год рождения, город рождения). 
В процессе работы программы в некотором кортеже poet_data обнаружилась ошибка: 
('Пушкин', 1799, 'Санкт-Петербург'). 
Тут неверно указано место рождения, 
ведь Александр Пушкин родился в Москве.

Дополните приведенный ниже код так, 
чтобы в переменной poet_data 
находился правильный кортеж 
(с исправленным значением), 
а затем выведите его.
'''

# example
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
print(poet_data)

# review 1
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = list(poet_data)
poet_data[-1] = "Москва"
poet_data = tuple(poet_data)
print(poet_data)

# review 2
poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
poet_data = poet_data[:-1] + ("Москва", )
print(poet_data)