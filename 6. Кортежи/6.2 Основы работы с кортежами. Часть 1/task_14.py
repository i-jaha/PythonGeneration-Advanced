'''
В переменную city_name вводится название города (например, Москва), 
а в переменную city_year – год его основания (например, 1147). 
Заполните пропущенную строку таким образом, 
чтобы в переменной city оказался кортеж 
из значений этих двух переменных (сначала название города, затем год основания).
'''

# example
city_name = input()
city_year = int(input())
city = ...
print(city)

# review
city_name = input()
city_year = int(input())
city = (city_name, city_year)
print(city)