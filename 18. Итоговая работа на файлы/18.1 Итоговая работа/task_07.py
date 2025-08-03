'''Транслитерация 🔁🌶️
Транслитерация – передача знаков одной письменности знаками другой письменности, 
при которой каждый знак 
(или последовательность знаков) 
одной системы письма передаётся соответствующим знаком 
(или последовательностью знаков) другой системы письма.

Вам доступен текстовый файл cyrillic.txt, 
содержащий текст. 
Напишите программу для транслитерации этого файла, 
то есть замены кириллических символов на латинские 
в соответствии с предложенной таблицей. 
Все остальные символы надо оставить без изменений. 
Результат транслитерации требуется записать в файл transliteration.txt.
    | Кириллица | Латиница | Кириллица | Латиница | Кириллица | Латиница |
    | --------- | -------- | --------- | -------- | --------- | -------- |
    | а         | a        | к         | k        | х         | h        |
    | б         | b        | л         | l        | ц         | c        |
    | в         | v        | м         | m        | ч         | ch       |
    | г         | g        | н         | n        | ш         | sh       |
    | д         | d        | о         | o        | щ         | shh      |
    | е         | e        | п         | p        | ъ         | *        |
    | ё         | jo       | р         | r        | ы         | y        |
    | ж         | zh       | с         | s        | ь         | '        |
    | з         | z        | т         | t        | э         | je       |
    | и         | i        | у         | u        | ю         | ju       |
    | й         | j        | ф         | f        | я         | ya       |

На вход программе ничего не подается.

Программа должна создать файл 
с именем transliteration.txt 
в соответствии с условием задачи.

Примечание 1. 
Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. 
Обратите внимание, что заглавные буквы должны заменяться 
на соответствующие им заглавные же буквы, 
но если транслитерационная последовательность состоит 
из нескольких символов, 
то заглавным будет только первый из них: 
«С» на «S», а «Я» на «Ya».

Примечание 3. 
Если бы файл cyrillic.txt содержал текст:
    Президент США Дональд Трамп продолжил обмен выпадами с руководством КНДР.
    We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.
то содержимое файла transliteration.txt будет:
    Prezident SShA Donal'd Tramp prodolzhil obmen vypadami s rukovodstvom KNDR.
    We all know why Joe Biden is rushing to falsely pose as the winner, and why his media allies are trying so hard to help him: they don’t want the truth to be exposed.

Примечание 4. 
Указанный файл можно скачать 
по [ссылке](https://stepik.org/media/attachments/lesson/448983/cyrillic.txt).
'''

table = {
    'а': 'a',  'б': 'b',  'в': 'v',  'г': 'g',  
    'д': 'd',  'е': 'e',  'ё': 'jo', 'ж': 'zh', 
    'з': 'z',  'и': 'i',  'й': 'j',  'к': 'k',  
    'л': 'l',  'м': 'm',  'н': 'n',  'о': 'o',  
    'п': 'p',  'р': 'r',  'с': 's',  'т': 't',  
    'у': 'u',  'ф': 'f',  'х': 'h',  'ц': 'c',  
    'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*',
    'ы': 'y',  'ь': "'",  'э': 'je', 'ю': 'ju', 
    'я': 'ya'
    }
with open("cyrillic.txt") as text:
    content = text.read()
result = ""
for char in content:
    lower = char.lower()
    if lower in table:
        trans = table[lower]
        result += trans.capitalize() if char.isupper() else trans
    else:
        result += char
with open("transliteration.txt", "w", encoding="utf-8") as out:
    out.write(result)