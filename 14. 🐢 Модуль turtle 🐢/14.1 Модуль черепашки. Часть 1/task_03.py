'''
Напишите программу, 
которая рисует правильный треугольник.

Примечание 1. 
Программу нужно оформить в виде 
функции triangle(side), 
где side – длина стороны треугольника в пикселях.

Примечание 2. 
Величина каждого угла правильного треугольника 
равна 60 градусам.
'''

import turtle

def triangle(side):
  turtle.shape('turtle')
  for _ in range(3):
    turtle.forward(side)
    turtle.left(120)


side = int(input())
triangle(side)