'''
Напишите программу, 
которая рисует прямоугольник.

Примечание. 
Программу нужно оформить 
в виде функции rectangle(width, height), 
где width, height – 
ширина и высота прямоугольника.
'''

import turtle

def rectangle(width, height):
  turtle.shape('turtle')
  for _ in range(2):
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)


width = int(input())
height = int(input())
rectangle(width, height)