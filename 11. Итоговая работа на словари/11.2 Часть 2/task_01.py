'''Минутка генетики 🧬
Как известно из курса биологии, ДНК и РНК – последовательности нуклеотидов.
Четыре нуклеотида в ДНК:
    аденин (A);
    цитозин (C);
    гуанин (G);
    тимин (T).
Четыре нуклеотида в РНК:
    аденин (A);
    цитозин (C);
    гуанин (G);
    урацил (U).
Цепь РНК строится на основе цепи ДНК 
последовательным присоединением комплементарных нуклеотидов:
    G → C;
    C → G;
    T → A;
    A → U.
Напишите программу, переводящую цепь ДНК в цепь РНК.

На вход программе подается корректная цепь ДНК в верхнем регистре.

Программа должна вывести соответствующую цепь РНК в верхнем регистре.

Примечание. 
Подробнее прочитать про ДНК и РНК можно 
по (ссылке)[https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%B7%D0%BE%D0%BA%D1%81%D0%B8%D1%80%D0%B8%D0%B1%D0%BE%D0%BD%D1%83%D0%BA%D0%BB%D0%B5%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82%D0%B0] 
и по (ссылке)[https://ru.wikipedia.org/wiki/%D0%A0%D0%B8%D0%B1%D0%BE%D0%BD%D1%83%D0%BA%D0%BB%D0%B5%D0%B8%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F_%D0%BA%D0%B8%D1%81%D0%BB%D0%BE%D1%82%D0%B0].
'''

# review 1
dna = ["G", "C", "T", "A"]
rna = ["C", "G", "A", "U"]
strand = dict(zip(dna, rna))
dna_input = input().strip()
for ch in dna_input:
    if ch in strand:
        print(strand[ch], end="")
    else:
        print("?", end="")

# review 2
print("".join(dict(zip(["G", "C", "T", "A"], ["C", "G", "A", "U"]))[ch] for ch in input().strip()))

# review 3
d = {'ACGT'[i]: 'UGCA'[i] for i in range(4)}
print(*[d[i] for i in input().strip()], sep='')