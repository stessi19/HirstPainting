# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg",30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import random
from turtle import Turtle, Screen
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (226, 198, 131), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.hideturtle()
tim.speed("fastest")
tim.teleport(-250,-250)
for x in range(10):
    for _ in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        print(tim.pos())
        tim.pendown()
    tim.teleport(-250,-250+50*(x+1))


screen.exitonclick()