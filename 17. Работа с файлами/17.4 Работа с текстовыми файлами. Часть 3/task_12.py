'''Загадка от Жака Фреско 🐐🌶️
Однажды Жака Фреско спросили:
    "Если ты такой умный, почему не богатый?"
Жак не стал отвечать на столь провокационный вопрос, 
вместо этого он задал загадку спрашивающему:
    "Были разноцветные козлы. Сколько?"
    "Сколько чего?"
    "Сколько из них составляет более 7% от общего количества козлов?"
Вам доступен текстовый файл goats.txt, 
в первой строке которого написано слово COLOURS, 
далее идет список всех возможных цветов козлов. 
Затем идет строка со словом GOATS, 
и далее непосредственно перечисление козлов разных цветов. 
Перечень козлов включает только строки из первого списка.
Напишите программу создания файла answer.txt 
и вывода в него списка козлов, 
которые удовлетворяют условию загадки от Жака Фреско.

На вход программе ничего не подается.

Программа должна создать файл с именем answer.txt 
и вывести в него в алфавитном порядке названия цветов козлов, 
которые удовлетворяют условию загадки Жака Фреско.

Примечание 1. 
Считайте, что исполняемая программа 
и указанные файлы находятся в одной папке.

Примечание 2. 
Если бы файл goats.txt содержал строки:
    COLOURS
    Pink goat
    Green goat
    Black goat
    GOATS
    Pink goat
    Pink goat
    Black goat
    Pink goat
    Pink goat
    Black goat
    Green goat
    Pink goat
    Black goat
    Black goat
    Pink goat
    Pink goat
    Black goat
    Black goat
    Pink goat
то файл answer.txt имел бы вид:
    Black goat
    Pink goat

Примечание 3. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/519126/goats.txt]. 
'''

# review 1
with open("goats.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

colours_index = lines.index("COLOURS")
goats_index = lines.index("GOATS")

colours = lines[colours_index + 1 : goats_index]
goats = lines[goats_index + 1 :]

goat_counts = {}
for colour in colours:
    goat_counts[colour] = 0

for goat in goats:
    if goat in goat_counts:
        goat_counts[goat] += 1

total_goats = len(goats)
threshold = total_goats * 0.07

popular_colours = []
for colour in colours:
    if goat_counts[colour] > threshold:
        popular_colours.append(colour)

popular_colours.sort()

with open("answer.txt", "w", encoding="utf-8") as out:
    for colour in popular_colours:
        out.write(colour + "\n")

# review 2
with open("goats.txt", "r", encoding="utf-8") as infile, \
    open("answer.txt", "w", encoding="utf-8") as outfile:
    cont = infile.read().split('\n')
    colors, goats = cont[1:cont.index('GOATS')], cont[cont.index('GOATS')+1:]
    print(*sorted(filter(lambda x: goats.count(x) / len(goats) > 0.07, colors)), sep='\n', file=outfile)