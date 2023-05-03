# 5.8 Koch curve

import turtle

fractal = 's+s-s+s'
n = int(input())
koch_curve = 's'
for i in range(n):
    koch_curve = ''.join([fractal if j == 's' else j
                          for j in list(koch_curve)])

res = [i for i in list(koch_curve) if i != 's']
[print('turn', ('60' if i == '+' else '-120')) for i in res]


size = 600
turtle.width(2)
turtle.pencolor('white')
turtle.bgcolor('black')
turtle.hideturtle()
turtle.penup()
turtle.setposition(-300, 0)
turtle.pendown()

step = size / (3**n)
for i in list(koch_curve):
    if i != 's':
        turtle.left(60 if i == '+' else -120)
    else:
        turtle.forward(step)

turtle.done()
