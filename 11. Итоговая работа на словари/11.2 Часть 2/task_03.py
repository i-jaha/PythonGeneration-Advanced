'''Scrabble game
В игре Scrabble 
каждая буква приносит определенное количество баллов. 
Общая стоимость слова – сумма баллов его букв. 
Чем реже буква встречается, тем больше она ценится:
    | Баллы | Буква                                  |
    | ----- | -------------------------------------- |
    | 1     | A, E, I, L, N, O, R, S, T, U           |
    | 2     | D, G                                   |
    | 3     | B, C, M, P                             |
    | 4     | F, H, V, W, Y                          |
    | 5     | K                                      |
    | 8     | J, X                                   |
    | 10    | Q, Z                                   |
Напишите программу подсчета итоговой стоимости введенного слова.

На вход программе подается одно слово в верхнем регистре на английском языке.

Программа должна вывести суммарную стоимость букв введенного слова.
'''

# review 1
scrabble = {
    'AEILNORSTU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
letter_score = {ch: score for letters, score in scrabble.items() for ch in letters}
word = input().strip().upper()
points = sum(letter_score.get(ch, 0) for ch in word)
print(points)

# review 2
scrabble = {
    'AEILNORSTU': 1,
    'DG': 2,
    'BCMP': 3,
    'FHVWY': 4,
    'K': 5,
    'JX': 8,
    'QZ': 10
}
print(sum([score for letters, score in scrabble.items() for letter in input().strip().upper() if letter in letters]))