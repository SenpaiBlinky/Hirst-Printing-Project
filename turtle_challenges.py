from turtle import Turtle, Screen
import turtle as t
# import heroes
from random import choice, randint

tim = Turtle()
tim.shape("turtle")
tim.color("purple")
pen_colors = ["purple1","salmon","maroon1","cyan","coral","yellow","green"]
directions = [0,90,180,270]

# tim.pencolor((50.0, 193.0, 143.0))



# ---------------------------------- draw a bunch of side-gons in different colors
# for i in range(3,20):
#     tim.pencolor(choice(pen_colors))
#     angle = 360 / i
#     for n in range(i):
#         tim.forward(69)
#         tim.right(angle)
        
# ------------------------------------ make a random walk
# tim.width(7)
# tim.speed(0)
# for i in range(0,1001):
#     tim.pencolor(choice(pen_colors))
#     tim.right(choice(directions))
#     tim.forward(30)

# ------------------------------------ make a random walk with random colors
# t.colormode(255)
# tim.width(7)
# def random_color():
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     return (r, g, b)

# tim.speed(0)
# for i in range(0,1001):
#     tim.pencolor(random_color())
#     tim.right(choice(directions))
#     tim.forward(30)

# -------------------------------------- drawing a spirograph

t.colormode(255) # ----------!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!
tim.width(3)
tim.speed(0)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r, g, b)


for i in range(0, 361, 6):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(6)





# ------------------------------- Final steps below -----------------------------
screen = Screen()
screen.exitonclick()
