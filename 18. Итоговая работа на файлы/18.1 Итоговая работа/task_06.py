'''Forbidden words 🤬🌶️
На вход программе подается строка текста 
с именем текстового файла. 
Напишите программу, 
выводящую на экран содержимое этого файла, 
но с заменой всех запрещенных слов звездочками * 
(количество звездочек равно количеству букв в слове).

Запрещенные слова, 
разделенные символом пробела, 
хранятся в текстовом файле forbidden_words.txt. 
Гарантируется, что все слова в этом файле записаны в нижнем регистре.

На вход программе подается строка текста 
с именем существующего текстового файла, 
в котором необходимо заменить запрещенные слова звездочками.

Программа должна вывести текст в соответствии с условием задачи.

Примечание 1. 
Ваша программа должна заменить запрещенные слова, 
где бы они ни встречались, 
даже если они встречаются в середине другого слова.

Примечание 2. 
Программа должна заменять запрещенные слова 
независимо от их регистра. 
Например, если файл forbidden_words.txt содержит запрещенное слово exam, 
то слова exam, Exam, ExaM, EXAM и подобные должны быть заменены на ****.

Примечание 3. 
Если бы файл forbidden_words.txt содержал слова:
    hello email python the exam wor is
а файл в котором заменяются слова имел бы вид:
    Hello, world! Python IS the programming language of thE future. My EMAIL is....
    PYTHON is awesome!!!!
то результатом будет:
    *****, ***ld! ****** ** *** programming language of *** future. My ***** **....
    ****** ** awesome!!!!

Примечание 4. 
Файл forbidden_words.txt можно скачать 
по [ссылке](https://stepik.org/media/attachments/lesson/448983/forbidden_words.txt). 
Ваша программа прогоняется на трех файлах 
[data.txt](https://stepik.org/media/attachments/lesson/448983/data.txt), 
[stepik.txt](https://stepik.org/media/attachments/lesson/448983/stepik.txt) 
и [beegeek.txt](https://stepik.org/media/attachments/lesson/448983/beegeek.txt).
'''

with open("forbidden_words.txt", encoding="utf-8") as f:
    forbidden = f.read().split()

filename = input()
with open(filename, encoding="utf-8") as f:
    text = f.read()
lower_text = text.lower()
mask = list(text)
for word in forbidden:
    lw = word.lower()
    start = 0
    while True:
        idx = lower_text.find(lw, start)
        if idx == -1:
            break
        for i in range(idx, idx + len(word)):
            mask[i] = '*'
        start = idx + 1
print(''.join(mask))
