"""
Список по образцу 2
На вход программе подается число n.
Напишите программу, которая создает и выводит построчно вложенный список,
состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
На вход программе подается натуральное число n.
Программа должна вывести построчно указанный вложенный список.
"""

# review 1
n = int(input())
my_list = []
for row in range(1, n+1):
    for elem in range(1, row + 1):
        my_list.append(elem)
    print(my_list)
    my_list.clear()


# review 2
n = int(input())
my_list = []
for row in range(1, n+1):
    my_list.append(list(range(1, row+1)))
print(*my_list, sep="\n")

# review 3
n = int(input())
print(*[[elem for elem in range(1, row+1)] for row in range(1, n+1)], sep="\n")