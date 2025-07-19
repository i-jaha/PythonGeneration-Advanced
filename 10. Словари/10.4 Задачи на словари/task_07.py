'''Секретное слово
Напишите программу для расшифровки секретного слова 
методом частотного анализа.

В первой строке задано зашифрованное слово. 
Во второй строке задано одно целое число n – 
количество букв в словаре. 
В следующих n строках записано, 
сколько раз конкретная буква алфавита встречается в этом слове – 
<буква>: <частота>.

Программа должна вывести дешифрованное слово.

Примечание. 
Гарантируется, что частоты букв не повторяются.
'''

# review 1
counter = {}
cipher_text = list(input().strip())
for c in cipher_text:
    counter[c] = counter.get(c, 0) + 1

dict_from_values = {}
for _ in range(int(input())):
    line = input().split(":")
    letter = line[0].strip()
    freq = int(line[1])
    dict_from_values[freq] = letter

for i in range(len(cipher_text)):
    cipher_text[i] = dict_from_values[counter[cipher_text[i]]]

print("".join(cipher_text))


# review 2
counter, dict_from_values = {}, {}
cipher_text = input()

for c in cipher_text:
    counter[c] = counter.get(c, 0) + 1

for _ in range(int(input())):
    letter, freq = input().split(': ')
    dict_from_values[int(freq)] = letter

for c in cipher_text:
    print(dict_from_values[counter[c]], end="")