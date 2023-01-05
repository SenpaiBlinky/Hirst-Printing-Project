from turtle import Turtle, Screen
import turtle as t
# import heroes
from random import choice, randint
import colorgram

t.colormode(255)

# colors = colorgram.extract("hirst.png", 20)
rgb_colors = [(208, 165, 125), (250, 235, 237), (140, 49, 106), (164, 169, 38), (244, 80, 57), (230, 114, 163), (3, 143, 55), (215, 234, 232), (241, 65, 140), (1, 143, 184), (162, 55, 52), (50, 203, 226), (254, 230, 0), (21, 166, 126), (245, 224, 47), (212, 235, 238), (28, 196, 219), (119, 184, 146), (231, 167, 191)]

tim = Turtle()
tim.hideturtle()
tim.shape("turtle")
tim.color("purple")
tim.penup()
tim.speed("fastest")
tim.backward(300)
tim.right(90)
tim.forward(200)
tim.left(90)


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
for column in range (10):
    for row in range(10):
        tim.forward(50)
        tim.dot(20, choice(rgb_colors))
    if column == 9:
        continue
    else:
        tim.left(90)
        tim.forward(50)
        tim.right(90)
        tim.backward(500)









# ------------------------------- Final steps below -----------------------------
screen = Screen()
screen.exitonclick()