'''Входная строка ⌨️
Напишите программу, 
которая считывает строку текста 
и записывает её в текстовый файл output.txt.

На вход программе подается строка текста.

Программа должна создать файл с именем output.txt 
и записать в него считанную строку текста.

Примечание. 
Считайте, что исполняемая программа 
и указанный файл находятся в одной папке.
'''

# review 1
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(input())

# review 2
print(input(), file=open("output.txt", "w", encoding="utf-8"))  # файл не закрыт

# review 3
f = open("output.txt", "w", encoding="utf-8")
print(input(), file=f)
f.close()