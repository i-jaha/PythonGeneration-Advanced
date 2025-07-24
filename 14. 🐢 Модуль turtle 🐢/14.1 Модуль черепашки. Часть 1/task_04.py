'''
Напишите программу, 
которая рисует изображенную фигуру, 
состоящую из трех квадратов.

Примечание 1. 
Напишите функцию square(side), 
где side – длина стороны квадрата в пикселях.

Примечание 2. 
Поэксперементируйте с углом поворота черепашки 
при переходе от одного квадрата к другому.


'''

import turtle


def square(side, angle, cnt):
    for _ in range(cnt):
        turtle.left(angle)
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

    turtle.done()


side = 100
angle = 20
cnt = 3

square(side, angle, cnt)