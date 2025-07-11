'''Ходы ферзя
На шахматной доске 8×8 стоит ферзь. 
Отметьте положение ферзя на доске и все клетки, которые бьет ферзь. 
Клетку, где стоит ферзь, отметьте буквой Q, 
клетки, которые бьет ферзь, отметьте символами *, 
остальные клетки заполните точками.

На вход программе подаются координаты ферзя 
на шахматной доске в шахматной нотации 
(то есть в виде e4, где сначала записывается номер столбца 
(буква от a до h, слева направо), 
затем номер строки (цифра от 1 до 8, снизу вверх)).

Программа должна вывести на экран изображение доски, разделяя элементы пробелами.
'''

# review 1
pos = input()
col = ord(pos[0]) - ord('a')
row = 8 - int(pos[1])

board = [["."] * 8 for _ in range(8)]

for i in range(8):
    board[row][i] = '*'
    board[i][col] = '*'
    if 0 <= row + i < 8 and 0 <= col + i < 8:
        board[row + i][col + i] = '*'
    if 0 <= row - i < 8 and 0 <= col - i < 8:
        board[row - i][col - i] = '*'
    if 0 <= row + i < 8 and 0 <= col - i < 8:
        board[row + i][col - i] = '*'
    if 0 <= row - i < 8 and 0 <= col + i < 8:
        board[row - i][col + i] = '*'

board[row][col] = 'Q'

for line in board:
    print(*line)




# review 2
col, row = input()
col = ord(col) - ord('a')
row = 8 - int(row)

board = [["."] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i == row or j == col:
            board[i][j] = "*"
        elif abs(i - row) == abs(j - col):
            board[i][j] = "*"

board[row][col] = 'Q'

for line in board:
    print(*line)