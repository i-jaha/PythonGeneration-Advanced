'''
Используя цикл for и встроенную функцию max(), 
дополните приведенный ниже код так, 
чтобы он выводил максимальный элемент среди всех элементов 
вложенных списков списка list1.
'''

# # example
# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = 
# print(maximum)

# example
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = max([max(i) for i in list1])
print(maximum)