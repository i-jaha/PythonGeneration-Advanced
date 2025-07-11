'''
Подсписки списка 🌶️🌶️
Подсписок – часть другого списка. 
Подсписок может содержать один элемент, несколько или даже ни одного. 
Например, [1], [2], [3] и [4] – подсписки списка [1, 2, 3, 4]. 
Список [2, 3] – подсписок списка [1, 2, 3, 4], 
но список [2, 4] не подсписок списка [1, 2, 3, 4], 
так как элементы 2 и 4 во втором списке не смежные 
(они разрываются элементом 3). 
Пустой список – подсписок любого списка. 
Сам список – подсписок самого себя, 
то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].
На вход программе подается строка текста, содержащая символы. 
Из данной строки формируется список. 
Напишите программу, которая выводит список, 
содержащий все возможные подсписки списка, включая пустой список.

На вход программе подается строка текста, 
содержащая символы, разделенные символом пробела.

Программа должна вывести указанный список, содержащий все возможные подсписки, 
включая пустой список в соответствии с примерами.

Примечание. 
Порядок списков одинаковой длины должен соответствовать 
порядку их вхождения в основной список.
'''

def get_all_sublists(lst):
    result = [[]]
    n = len(lst)
    for size in range(1, n + 1):
        cur_seq = []
        for i in range(n - size + 1):
            cur_seq.append(lst[i : (i+size)])
        result.extend(cur_seq)
    return result

data = input().split()
print(get_all_sublists(data))