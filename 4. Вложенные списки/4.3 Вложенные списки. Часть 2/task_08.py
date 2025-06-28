'''
Список по образцу 1
На вход программе подается число n. 
Напишите программу, которая создает и выводит построчно список, 
состоящий из n списков 
[[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
На вход программе подается натуральное число n.
Программа должна вывести построчно указанный список.
'''

# review 1
n = int(input())
my_list = []
for row in range(n):
    for elem in range(1, n+1):
        my_list.append(elem)
    print(my_list)
    my_list.clear()

# review 2
n = int(input())
my_list = []
for row in range(n):
    my_list.append(list(range(1, n+1)))
print(*my_list, sep="\n")

# review 3
n = int(input())
print(*[[elem for elem in range(1, n+1)] for row in range(n)], sep="\n")