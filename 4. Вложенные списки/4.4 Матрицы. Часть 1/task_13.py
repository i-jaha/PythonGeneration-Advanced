'''
Максимальный в области 2 🌶️
Напишите программу, которая выводит максимальный элемент 
в заштрихованной области квадратной матрицы.
    :-----------------------------------------------.
    =::.                                         .:+.
    =::::.                                     .::.=.
    =..::::.                                 .::.::=.
    =::.::.::.                             .::..:..=.
    =.::..:..:..                         .::..:..::=.
    =:..:..::.::.                       .:..:..::.:+.
    =.:..::.::..-:.                   .:..::.::.::.=.
    =:.::.::..-..:::.               .:..-:.::..:..:=.
    =::..:..:..::..:.:.           .:..::..:..:..::.=.
    =..:..::.::..-..:..:.       .::.::..-..:..::.::=.
    =-..::.::..-..::.::.::.   .::.::..:..-..::.::..+.
    =.::.::..-..::.::..:..-: ::..:..:..-:.::..:..:.=.
    =-..:..:..::..-..:..-..:::.-..::.::..-..:..::.:+.
    =.:..::.::..-..::.::.:.  .::::.::..-..-..::.::.=.
    =:.::.::..-..::.::.:.      .:::..:..-..::..:..:=.
    =::.::..:..::.::.:.          .:-..::.::..:..:..=.
    =..:..::.::..-...              .::..-..:..::.::=.
    =-..::.::..-..:                  .-..:..::.::..+.
    =.::.::..:..:                      .:.::..:..:.=.
    =:..:..:..:.                         .:.:..:..:+.
    =::..::.:.                            ..:::.::.=.
    =:.::.:.                                ..::..:=.
    =::...                                    ..:..=.
    =::.                                        .::=.
    :-----------------------------------------------.

На вход программе подается натуральное число n – 
количество строк и столбцов в матрице, 
затем элементы матрицы (целые числа) построчно через пробел.

Программа должна вывести одно число – 
максимальный элемент в заштрихованной области квадратной матрицы.
'''

n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
mx = matrix[0][0]
for r in range(n):
    for c in range(n):
        if (r >= c and r <= n - 1 - c) or (r <= c and r >= n - 1 - c):
            if matrix[r][c] > mx:
                mx = matrix[r][c]
print(mx)