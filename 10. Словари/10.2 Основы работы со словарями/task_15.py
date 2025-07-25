'''Набор сообщений 📩
На мобильных кнопочных телефонах 
текстовые сообщения можно отправлять 
с помощью цифровой клавиатуры. 
Поскольку с каждой клавишей связано несколько букв, 
для большинства букв требуется несколько нажатий клавиш. 
При однократном нажатии цифры генерируется первый символ, 
указанный для этой клавиши. 
Нажатие цифры 2,3,4 или 5 раз 
генерирует второй, третий, четвертый или пятый символ клавиши.
| 1 | `.,?!:`          |
| 2 | `ABC`            |
| 3 | `DEF`            |
| 4 | `GHI`            |
| 5 | `JKL`            |
| 6 | `MNO`            |
| 7 | `PQRS`           |
| 8 | `TUV`            |
| 9 | `WXYZ`           |
| 0 | `space (пробел)` |

Напишите программу, 
которая отображает нажатия клавиш, 
необходимые для введенного сообщения.

На вход программе подается одна строка – 
текстовое сообщение.

Программа должна вывести нажатия клавиш, 
необходимых для введенного сообщения.

Примечание 1. 
Ваша программа должна обрабатывать как прописные, 
так и строчные буквы.

Примечание 2. 
Ваша программа должна игнорировать любые символы, 
не указанные в приведенной выше таблице.
'''

keypad = {
    "1": ".,?!:",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": " "
}

message = input().upper()
result = ""
for char in message:
    for key, chars in keypad.items():
        if char in chars:
            presses = chars.index(char) + 1
            result += key * presses
            break
print(result)